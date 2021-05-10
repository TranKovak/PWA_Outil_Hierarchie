# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info_popup.ui'
##
## Created by: Qt User Interface Compiler version 6.0.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_info(object):
    def setupUi(self, info):
        if not info.objectName():
            info.setObjectName(u"info")
        info.resize(400, 120)
        self.verticalLayout = QVBoxLayout(info)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(info)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(info)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(info)

        QMetaObject.connectSlotsByName(info)
    # setupUi

    def retranslateUi(self, info):
        info.setWindowTitle(QCoreApplication.translate("info", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("info", u"OK", None))
    # retranslateUi

