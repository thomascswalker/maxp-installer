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
        MainWindow.resize(550, 405)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(550, 320))
        MainWindow.setMaximumSize(QSize(550, 550))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
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

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.packages = QTableWidget(self.centralwidget)
        if (self.packages.columnCount() < 2):
            self.packages.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.packages.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.packages.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.packages.setObjectName(u"packages")
        self.packages.setColumnCount(2)
        self.packages.horizontalHeader().setDefaultSectionSize(100)
        self.packages.horizontalHeader().setStretchLastSection(True)
        self.packages.verticalHeader().setVisible(False)
        self.packages.verticalHeader().setMinimumSectionSize(20)
        self.packages.verticalHeader().setHighlightSections(False)

        self.gridLayout.addWidget(self.packages, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 20, -1, -1)
        self.maxVersionList = QComboBox(self.centralwidget)
        self.maxVersionList.setObjectName(u"maxVersionList")

        self.horizontalLayout.addWidget(self.maxVersionList)

        self.maxVersionExplore = QToolButton(self.centralwidget)
        self.maxVersionExplore.setObjectName(u"maxVersionExplore")

        self.horizontalLayout.addWidget(self.maxVersionExplore)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setTextFormat(Qt.AutoText)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.installPath = QLabel(self.centralwidget)
        self.installPath.setObjectName(u"installPath")
        self.installPath.setTextFormat(Qt.RichText)
        self.installPath.setWordWrap(False)

        self.horizontalLayout_4.addWidget(self.installPath)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Better Max Tools</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"This will install the better-max-tools package into an environment accessible by 3ds Max.", None))
        ___qtablewidgetitem = self.packages.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.packages.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Version", None));
        self.maxVersionExplore.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Install location:", None))
        self.installPath.setText("")
    # retranslateUi

