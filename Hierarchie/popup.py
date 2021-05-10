# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup.ui'
##
## Created by: Qt User Interface Compiler version 6.0.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 147)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.question_textBrowser = QTextBrowser(Dialog)
        self.question_textBrowser.setObjectName(u"question_textBrowser")

        self.verticalLayout.addWidget(self.question_textBrowser)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancel_button = QPushButton(Dialog)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout.addWidget(self.cancel_button)

        self.validation_button = QPushButton(Dialog)
        self.validation_button.setObjectName(u"validation_button")

        self.horizontalLayout.addWidget(self.validation_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.cancel_button.setText(QCoreApplication.translate("Dialog", u"Annuler", None))
        self.validation_button.setText(QCoreApplication.translate("Dialog", u"Valider", None))
    # retranslateUi

