# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import ressources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(512, 299)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 50))
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setPixmap(QPixmap(u":/mainUi/Ressources/office-building.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.group_comboBox = QComboBox(self.centralwidget)
        self.group_comboBox.setObjectName(u"group_comboBox")

        self.verticalLayout_2.addWidget(self.group_comboBox)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.companies_comboBox = QComboBox(self.centralwidget)
        self.companies_comboBox.setObjectName(u"companies_comboBox")

        self.verticalLayout_2.addWidget(self.companies_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.getHierarchy_button = QPushButton(self.centralwidget)
        self.getHierarchy_button.setObjectName(u"getHierarchy_button")

        self.verticalLayout.addWidget(self.getHierarchy_button)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 50))
        self.label_2.setMaximumSize(QSize(50, 50))
        self.label_2.setPixmap(QPixmap(u":/mainUi/Ressources/excel.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.get_excel_file_button = QPushButton(self.centralwidget)
        self.get_excel_file_button.setObjectName(u"get_excel_file_button")

        self.horizontalLayout_3.addWidget(self.get_excel_file_button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.set_hierarchy_button = QPushButton(self.centralwidget)
        self.set_hierarchy_button.setObjectName(u"set_hierarchy_button")

        self.verticalLayout.addWidget(self.set_hierarchy_button)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Choix groupe :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Choix entreprise :", None))
        self.getHierarchy_button.setText(QCoreApplication.translate("MainWindow", u"R\u00e9cup\u00e9rer la hi\u00e9rarchie", None))
        self.label_2.setText("")
        self.get_excel_file_button.setText(QCoreApplication.translate("MainWindow", u"Choisir le fichier excel", None))
        self.set_hierarchy_button.setText(QCoreApplication.translate("MainWindow", u"Modifier la hi\u00e9rarchie \u00e0 partir du fichier excel", None))
    # retranslateUi

