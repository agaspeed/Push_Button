# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ce_login_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Main_window(object):
    def setupUi(self, Main_window):
        if not Main_window.objectName():
            Main_window.setObjectName(u"Main_window")
        Main_window.resize(810, 499)
        self.gridLayout_2 = QGridLayout(Main_window)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(9)
        self.gridLayout_2.setVerticalSpacing(6)
        self.verticalSpacer_top = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_top, 0, 1, 1, 1)

        self.verticalSpacer_bottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_bottom, 2, 1, 1, 1)

        self.stackedWidget_main = QStackedWidget(Main_window)
        self.stackedWidget_main.setObjectName(u"stackedWidget_main")
        self.stackedWidget_main.setFrameShape(QFrame.NoFrame)
        self.stackedWidget_main.setFrameShadow(QFrame.Sunken)
        self.page_username = QWidget()
        self.page_username.setObjectName(u"page_username")
        self.horizontalLayout_3 = QHBoxLayout(self.page_username)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEditpassword = QLineEdit(self.page_username)
        self.lineEditpassword.setObjectName(u"lineEditpassword")
        self.lineEditpassword.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.lineEditpassword, 2, 1, 1, 1)

        self.lineEdit_username = QLineEdit(self.page_username)
        self.lineEdit_username.setObjectName(u"lineEdit_username")

        self.gridLayout.addWidget(self.lineEdit_username, 1, 1, 1, 1)

        self.label_username = QLabel(self.page_username)
        self.label_username.setObjectName(u"label_username")

        self.gridLayout.addWidget(self.label_username, 1, 0, 1, 1)

        self.label_password = QLabel(self.page_username)
        self.label_password.setObjectName(u"label_password")

        self.gridLayout.addWidget(self.label_password, 2, 0, 1, 1)

        self.page1_user_input = QHBoxLayout()
        self.page1_user_input.setSpacing(6)
        self.page1_user_input.setObjectName(u"page1_user_input")
        self.page1_user_input.setSizeConstraint(QLayout.SetNoConstraint)
        self.pushButton_cancel = QPushButton(self.page_username)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.page1_user_input.addWidget(self.pushButton_cancel)

        self.pushButton_login_user = QPushButton(self.page_username)
        self.pushButton_login_user.setObjectName(u"pushButton_login_user")

        self.page1_user_input.addWidget(self.pushButton_login_user)


        self.gridLayout.addLayout(self.page1_user_input, 3, 1, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout)

        self.stackedWidget_main.addWidget(self.page_username)
        self.page_welcome = QWidget()
        self.page_welcome.setObjectName(u"page_welcome")
        self.verticalLayout = QVBoxLayout(self.page_welcome)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_dynamic_username = QLabel(self.page_welcome)
        self.label_dynamic_username.setObjectName(u"label_dynamic_username")
        self.label_dynamic_username.setScaledContents(True)
        self.label_dynamic_username.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_dynamic_username)

        self.label_welcome = QLabel(self.page_welcome)
        self.label_welcome.setObjectName(u"label_welcome")
        self.label_welcome.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_welcome)

        self.stackedWidget_main.addWidget(self.page_welcome)
        self.page_wrong_password = QWidget()
        self.page_wrong_password.setObjectName(u"page_wrong_password")
        self.label_wrong_password_msg = QLabel(self.page_wrong_password)
        self.label_wrong_password_msg.setObjectName(u"label_wrong_password_msg")
        self.label_wrong_password_msg.setGeometry(QRect(160, 20, 231, 111))
        self.label_wrong_password_msg.setAutoFillBackground(True)
        self.label_wrong_password_msg.setAlignment(Qt.AlignCenter)
        self.label_wrong_password_msg.setWordWrap(True)
        self.stackedWidget_main.addWidget(self.page_wrong_password)

        self.gridLayout_2.addWidget(self.stackedWidget_main, 1, 1, 1, 1)

        self.logo_ce = QLabel(Main_window)
        self.logo_ce.setObjectName(u"logo_ce")
        self.logo_ce.setPixmap(QPixmap(u"../../../../Downloads/CE logo.png"))
        self.logo_ce.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_2.addWidget(self.logo_ce, 0, 0, 1, 1)

        self.horizontalSpacer_right = QSpacerItem(90, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_right, 1, 2, 1, 1)

        QWidget.setTabOrder(self.lineEdit_username, self.lineEditpassword)
        QWidget.setTabOrder(self.lineEditpassword, self.pushButton_cancel)
        QWidget.setTabOrder(self.pushButton_cancel, self.pushButton_login_user)

        self.retranslateUi(Main_window)

        self.stackedWidget_main.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Main_window)
    # setupUi

    def retranslateUi(self, Main_window):
        Main_window.setWindowTitle(QCoreApplication.translate("Main_window", u"Dialog", None))
        self.label_username.setText(QCoreApplication.translate("Main_window", u"Username", None))
        self.label_password.setText(QCoreApplication.translate("Main_window", u"Password", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Main_window", u"Cancel", None))
        self.pushButton_login_user.setText(QCoreApplication.translate("Main_window", u"Login", None))
        self.label_dynamic_username.setText(QCoreApplication.translate("Main_window", u"Username", None))
        self.label_welcome.setText(QCoreApplication.translate("Main_window", u"Welcome to Creative Electron!", None))
        self.label_wrong_password_msg.setText(QCoreApplication.translate("Main_window", u"Sorry, your password and username do not match. Please try typing your password again. ", None))
        self.logo_ce.setText("")
    # retranslateUi
