from glob import glob
import os
from shutil import ExecError
import sys
import subprocess
from typing import List, Tuple
from collections import namedtuple

from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QTextStream
from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableWidgetItem,
)

import resources  # noqa: F401


APPLICATION_PLUGINS_PATH = r"C:\ProgramData\Autodesk\ApplicationPlugins"
AUTODESK_PATH = r"C:\Program Files\Autodesk"
SITE_PACKAGES = os.path.join(os.getenv("appdata"), r"Python\Python37\site-packages")

MaxInstall = namedtuple(
    "MaxInstall", ["directory", "version", "pythonExecutable", "sitePackages"]
)

def getMaxInstallations() -> List[Tuple[str]]:
    dirs = glob(AUTODESK_PATH + r"\3ds Max*")
    result = []

    for dir in dirs:
        if os.path.exists(os.path.join(dir, "3dsmax.exe")):
            version = int(dir.split(" ")[-1])
            appdata = os.getenv("appdata")

            if version == 2022:
                pythonExecutable = os.path.join(dir, r"Python37\python.exe")
                sitePackages = os.path.join(appdata, r"Python\Python37\site-packages")
            elif version == 2023:
                pythonExecutable = os.path.join(dir, r"Python\python.exe")
                sitePackages = os.path.join(appdata, r"Python\Python39\site-packages")
            else:
                return []

            install = MaxInstall(dir, version, pythonExecutable, sitePackages)
            result.append(install)

    return result


def isPackageInstalled(install: MaxInstall) -> bool:
    args = [install.pythonExecutable, "-m", "pip", "list"]
    result = subprocess.check_output(args)
    for line in result.decode().split("\n"):
        if "better-max-tools" in line:
            return True

    return False


def getInstalledPackages(install: MaxInstall) -> list:
    interpreter = install.pythonExecutable
    if not os.path.exists(interpreter):
        raise FileNotFoundError("Python interpreter not found.")

    p = subprocess.Popen(f"\"{interpreter}\" -m ensurepip", stdout=subprocess.PIPE, shell=True)
    (output, error) = p.communicate()

    p.wait()

    if error is not None:
        raise ExecError(output)

    packages = []
    args = [interpreter, "-m", "pip", "list"]

    result = subprocess.check_output(args)

    for line in result.decode().split("\n"):
        packages.append(line)

    return packages


def installPackage(install: MaxInstall, package: str) -> bool:
    interpreter = install.pythonExecutable
    if not os.path.exists(interpreter):
        raise FileNotFoundError("Python interpreter not found.")

    args = [interpreter, "-m", "pip", "install", package]
    subprocess.check_output(args)

    QMessageBox.information(None, "Better Max Tools", "Installed!")

    return True


def uninstallPackage(install: MaxInstall, package: str) -> bool:
    interpreter = install.pythonExecutable
    if not os.path.exists(interpreter):
        raise FileNotFoundError("Python interpreter not found.")

    args = [interpreter, "-m", "pip", "uninstall", "-y", package]
    subprocess.check_output(args)

    QMessageBox.information(None, "Better Max Tools", "Uninstalled!")

    return True


class InstallerWindow(QMainWindow):
    _installations: List[MaxInstall] = getMaxInstallations()
    _currentInstall: MaxInstall = _installations[0]
    _packageColumns: dict = {'name': 0, 'version': 1, 'update': 2, 'uninstall': 3}

    def __init__(self) -> None:
        super().__init__()

        # Import the UI, either from a .ui file or a compiled .py file
        try:
            from ui import Ui_MainWindow  # type: ignore
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
        except ImportError:
            uiFileName = os.path.join(os.path.dirname(__file__), "installer.ui")
            file = QFile(uiFileName)
            file.open(QFile.ReadOnly)

            loader = QUiLoader()
            self.ui = loader.load(file, None)
            self.setCentralWidget(self.ui.centralWidget())
            file.close()

        # Set default properties
        self.setWindowTitle("maxp Installer")

        # Run setup methods
        self.setupConnections()
        self.setupStyle()

        # Refresh the Ui
        self.refreshUi()

    def refreshUi(self) -> None:
        # Update the installation combo box with installed 3ds Max versions
        for installation in self._installations:
            name = f"3ds Max {installation.version}"
            data = installation.directory
            self.ui.maxVersionList.addItem(name, data)

        # Clear the current package list
        self.ui.packages.setRowCount(0)
        self.ui.packages.clear()

        # Get the list of currently-installed packages
        # The first entry will be "-------" so we'll skip that
        packages = getInstalledPackages(self._currentInstall)[1:]
        for package in packages:

            # Split the package into its elements: name, version
            elements = package.split()

            # If the split didn't work, continue
            if len(elements) < 2:
                continue

            # Extract the name and version
            name = elements[0]
            version = elements[1]

            # If either is invalid, continue
            if name is None or version is None:
                continue

            # Add a new row to the table
            index = self.ui.packages.rowCount()
            self.ui.packages.insertRow(index)
            index -= 1

            # Create a table item for the name and version
            nameItem = QTableWidgetItem(name)
            versionItem = QTableWidgetItem(version)

            # Set the current row's columns to the name and version
            nameCol = self._packageColumns['name']
            versionCol = self._packageColumns['version']
            updateCol = self._packageColumns['update']
            uninstallCol = self._packageColumns['uninstall']

            self.ui.packages.setItem(index, nameCol, nameItem)
            self.ui.packages.setItem(index, versionCol, versionItem)

            updateBtn = QPushButton('Update')
            self.ui.packages.setCellWidget(index, updateCol, updateBtn)

            uninstallBtn = QPushButton('Uninstall')
            self.ui.packages.setCellWidget(index, uninstallCol, uninstallBtn)

        self.ui.installPath.setText(self._currentInstall.sitePackages)

    def setupConnections(self) -> None:
        self.ui.btnExploreMax.clicked.connect(self.exploreMaxVersion)
        self.ui.btnExplorePython.clicked.connect(self.explorePythonPackages)
        self.ui.toolButton.clicked.connect(self.installClicked)

    def setupStyle(self) -> None:
        file = QFile(os.path.join(os.path.dirname(__file__), "adsk_dark.qss"))
        file.open(QFile.ReadOnly)
        stream = QTextStream(file)
        content = stream.readAll()
        file.close()
        self.setStyleSheet(content)

    def exploreMaxVersion(self) -> None:
        path = self.ui.maxVersionList.currentData()
        if os.path.exists(path):
            subprocess.Popen(f'explorer "{path}"')

    def explorePythonPackages(self) -> None:
        path = self._currentInstall.sitePackages
        if os.path.exists(path):
            subprocess.Popen(f'explorer "{path}"')

    def installClicked(self):
        package = self.ui.lineEdit.text()
        installPackage(self._currentInstall, package)
        self.refreshUi()


def main() -> None:
    app = QApplication(sys.argv)

    dialog = InstallerWindow()
    dialog.show()

    app.exec_()


if __name__ == "__main__":
    main()
