# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'installer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(550, 536)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(550, 320))
        MainWindow.setMaximumSize(QSize(550, 550))
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.toolButton = QToolButton(self.groupBox_2)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_2.addWidget(self.toolButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.packages = QTableWidget(self.groupBox_2)
        if (self.packages.columnCount() < 4):
            self.packages.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.packages.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.packages.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.packages.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.packages.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.packages.setObjectName(u"packages")
        self.packages.setAlternatingRowColors(False)
        self.packages.setSelectionMode(QAbstractItemView.SingleSelection)
        self.packages.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.packages.setColumnCount(4)
        self.packages.horizontalHeader().setVisible(False)
        self.packages.horizontalHeader().setDefaultSectionSize(100)
        self.packages.horizontalHeader().setStretchLastSection(True)
        self.packages.verticalHeader().setVisible(False)
        self.packages.verticalHeader().setMinimumSectionSize(20)
        self.packages.verticalHeader().setHighlightSections(False)

        self.verticalLayout_3.addWidget(self.packages)


        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setTextFormat(Qt.RichText)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.maxVersionList = QComboBox(self.groupBox)
        self.maxVersionList.setObjectName(u"maxVersionList")

        self.horizontalLayout.addWidget(self.maxVersionList)

        self.btnExploreMax = QToolButton(self.groupBox)
        self.btnExploreMax.setObjectName(u"btnExploreMax")

        self.horizontalLayout.addWidget(self.btnExploreMax)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setTextFormat(Qt.AutoText)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.installPath = QLabel(self.groupBox)
        self.installPath.setObjectName(u"installPath")
        self.installPath.setTextFormat(Qt.RichText)
        self.installPath.setWordWrap(False)

        self.horizontalLayout_4.addWidget(self.installPath)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.btnExplorePython = QToolButton(self.groupBox)
        self.btnExplorePython.setObjectName(u"btnExplorePython")

        self.horizontalLayout_4.addWidget(self.btnExplorePython)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout.addWidget(self.spinBox, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Packages", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"Install", None))
        ___qtablewidgetitem = self.packages.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.packages.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Version", None));
        ___qtablewidgetitem2 = self.packages.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Update", None));
        ___qtablewidgetitem3 = self.packages.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Uninstall", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">3ds Max Python Package Explorer</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>This will show all installed packages for the selected 3ds Max version as well as aid in installing third party packages.</p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"3ds Max Versions", None))
        self.btnExploreMax.setText(QCoreApplication.translate("MainWindow", u"Explore", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Install location:", None))
        self.installPath.setText("")
        self.btnExplorePython.setText(QCoreApplication.translate("MainWindow", u"Explore", None))
    # retranslateUi

