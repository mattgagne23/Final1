# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_WelcomeWindow(object):
    def setupUi(self, WelcomeWindow):
        WelcomeWindow.setObjectName("WelcomeWindow")
        WelcomeWindow.resize(375, 450)
        WelcomeWindow.setStyleSheet("background-color: rgb(126, 132, 107);")
        self.centralwidget = QtWidgets.QWidget(parent=WelcomeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-10, 90, 361, 351))
        self.stackedWidget.setObjectName("stackedWidget")
        self.welcome = QtWidgets.QWidget()
        self.welcome.setObjectName("welcome")
        self.login_Label = QtWidgets.QLabel(parent=self.welcome)
        self.login_Label.setGeometry(QtCore.QRect(20, 20, 331, 20))
        self.login_Label.setObjectName("login_Label")
        self.name_Label = QtWidgets.QLabel(parent=self.welcome)
        self.name_Label.setGeometry(QtCore.QRect(80, 80, 51, 21))
        self.name_Label.setObjectName("name_Label")
        self.name_Edit = QtWidgets.QLineEdit(parent=self.welcome)
        self.name_Edit.setGeometry(QtCore.QRect(160, 80, 113, 20))
        self.name_Edit.setStyleSheet("background-color: rgb(208, 221, 215);")
        self.name_Edit.setObjectName("name_Edit")
        self.PIN_Label = QtWidgets.QLabel(parent=self.welcome)
        self.PIN_Label.setGeometry(QtCore.QRect(80, 120, 61, 21))
        self.PIN_Label.setObjectName("PIN_Label")
        self.PIN_Edit = QtWidgets.QLineEdit(parent=self.welcome)
        self.PIN_Edit.setGeometry(QtCore.QRect(160, 120, 113, 20))
        self.PIN_Edit.setStyleSheet("background-color: rgb(208, 221, 215);")
        self.PIN_Edit.setObjectName("PIN_Edit")
        self.accountType_Label = QtWidgets.QLabel(parent=self.welcome)
        self.accountType_Label.setGeometry(QtCore.QRect(60, 160, 101, 41))
        self.accountType_Label.setObjectName("accountType_Label")
        self.checking_Radio = QtWidgets.QRadioButton(parent=self.welcome)
        self.checking_Radio.setGeometry(QtCore.QRect(170, 170, 71, 21))
        self.checking_Radio.setObjectName("checking_Radio")
        self.account_radio_group = QtWidgets.QButtonGroup(WelcomeWindow)
        self.account_radio_group.setObjectName("account_radio_group")
        self.account_radio_group.addButton(self.checking_Radio)
        self.savings_Radio = QtWidgets.QRadioButton(parent=self.welcome)
        self.savings_Radio.setGeometry(QtCore.QRect(250, 170, 81, 21))
        self.savings_Radio.setObjectName("savings_Radio")
        self.account_radio_group.addButton(self.savings_Radio)
        self.login_button = QtWidgets.QPushButton(parent=self.welcome)
        self.login_button.setGeometry(QtCore.QRect(140, 210, 81, 21))
        self.login_button.setStyleSheet("background-color: rgb(89, 78, 54);")
        self.login_button.setObjectName("login_button")
        self.register_Label = QtWidgets.QLabel(parent=self.welcome)
        self.register_Label.setGeometry(QtCore.QRect(30, 250, 311, 21))
        self.register_Label.setObjectName("register_Label")
        self.register_button = QtWidgets.QPushButton(parent=self.welcome)
        self.register_button.setGeometry(QtCore.QRect(140, 290, 81, 21))
        self.register_button.setStyleSheet("background-color: rgb(89, 78, 54);")
        self.register_button.setObjectName("register_button")
        self.account_selection_label = QtWidgets.QLabel(parent=self.welcome)
        self.account_selection_label.setGeometry(QtCore.QRect(110, 190, 171, 20))
        self.account_selection_label.setText("")
        self.account_selection_label.setObjectName("account_selection_label")
        self.login_error_label = QtWidgets.QLabel(parent=self.welcome)
        self.login_error_label.setGeometry(QtCore.QRect(90, 230, 231, 20))
        self.login_error_label.setObjectName("login_error_label")
        self.register_error_label = QtWidgets.QLabel(parent=self.welcome)
        self.register_error_label.setGeometry(QtCore.QRect(110, 320, 191, 16))
        self.register_error_label.setObjectName("register_error_label")
        self.stackedWidget.addWidget(self.welcome)
        self.checking = QtWidgets.QWidget()
        self.checking.setObjectName("checking")
        self.balance_Label = QtWidgets.QLabel(parent=self.checking)
        self.balance_Label.setGeometry(QtCore.QRect(30, 10, 341, 41))
        self.balance_Label.setObjectName("balance_Label")
        self.action_requestLabel = QtWidgets.QLabel(parent=self.checking)
        self.action_requestLabel.setGeometry(QtCore.QRect(40, 60, 271, 20))
        self.action_requestLabel.setObjectName("action_requestLabel")
        self.deposit_amtLabel = QtWidgets.QLabel(parent=self.checking)
        self.deposit_amtLabel.setGeometry(QtCore.QRect(60, 90, 101, 21))
        self.deposit_amtLabel.setObjectName("deposit_amtLabel")
        self.deposit_inputEdit = QtWidgets.QLineEdit(parent=self.checking)
        self.deposit_inputEdit.setGeometry(QtCore.QRect(180, 90, 113, 20))
        self.deposit_inputEdit.setStyleSheet("background-color: rgb(208, 221, 215);")
        self.deposit_inputEdit.setObjectName("deposit_inputEdit")
        self.deposit_Button = QtWidgets.QPushButton(parent=self.checking)
        self.deposit_Button.setGeometry(QtCore.QRect(100, 130, 181, 20))
        self.deposit_Button.setStyleSheet("background-color: rgb(89, 78, 54);")
        self.deposit_Button.setObjectName("deposit_Button")
        self.withdrawl_amtLabel = QtWidgets.QLabel(parent=self.checking)
        self.withdrawl_amtLabel.setGeometry(QtCore.QRect(60, 180, 91, 20))
        self.withdrawl_amtLabel.setObjectName("withdrawl_amtLabel")
        self.withdrawal_inputEdit = QtWidgets.QLineEdit(parent=self.checking)
        self.withdrawal_inputEdit.setGeometry(QtCore.QRect(180, 180, 113, 20))
        self.withdrawal_inputEdit.setStyleSheet("background-color: rgb(208, 221, 215);")
        self.withdrawal_inputEdit.setObjectName("withdrawal_inputEdit")
        self.withdrawal_Button = QtWidgets.QPushButton(parent=self.checking)
        self.withdrawal_Button.setGeometry(QtCore.QRect(100, 220, 181, 20))
        self.withdrawal_Button.setStyleSheet("background-color: rgb(89, 78, 54);")
        self.withdrawal_Button.setObjectName("withdrawal_Button")
        self.statement_Button = QtWidgets.QPushButton(parent=self.checking)
        self.statement_Button.setGeometry(QtCore.QRect(90, 260, 201, 20))
        self.statement_Button.setStyleSheet("background-color: rgb(89, 78, 54);")
        self.statement_Button.setObjectName("statement_Button")
        self.savings_pageButton = QtWidgets.QPushButton(parent=self.checking)
        self.savings_pageButton.setGeometry(QtCore.QRect(50, 300, 111, 21))
        self.savings_pageButton.setStyleSheet("background-color: rgb(89, 78, 54);")
        self.savings_pageButton.setObjectName("savings_pageButton")
        self.login_pageButton = QtWidgets.QPushButton(parent=self.checking)
        self.login_pageButton.setGeometry(QtCore.QRect(240, 300, 101, 21))
        self.login_pageButton.setStyleSheet("background-color: rgb(89, 78, 54);")
        self.login_pageButton.setObjectName("login_pageButton")
        self.stackedWidget.addWidget(self.checking)
        self.savings = QtWidgets.QWidget()
        self.savings.setObjectName("savings")
        self.balance_Label_2 = QtWidgets.QLabel(parent=self.savings)
        self.balance_Label_2.setGeometry(QtCore.QRect(30, 10, 341, 41))
        self.balance_Label_2.setObjectName("balance_Label_2")
        self.statement_Button_2 = QtWidgets.QPushButton(parent=self.savings)
        self.statement_Button_2.setGeometry(QtCore.QRect(90, 260, 201, 20))
        self.statement_Button_2.setStyleSheet("background-color: rgb(89, 78, 54);")
        self.statement_Button_2.setObjectName("statement_Button_2")
        self.withdrawal_Button_2 = QtWidgets.QPushButton(parent=self.savings)
        self.withdrawal_Button_2.setGeometry(QtCore.QRect(100, 220, 181, 20))
        self.withdrawal_Button_2.setStyleSheet("background-color: rgb(89, 78, 54);")
        self.withdrawal_Button_2.setObjectName("withdrawal_Button_2")
        self.deposit_Button_2 = QtWidgets.QPushButton(parent=self.savings)
        self.deposit_Button_2.setGeometry(QtCore.QRect(100, 130, 181, 20))
        self.deposit_Button_2.setStyleSheet("background-color: rgb(89, 78, 54);")
        self.deposit_Button_2.setObjectName("deposit_Button_2")
        self.deposit_amtLabel_2 = QtWidgets.QLabel(parent=self.savings)
        self.deposit_amtLabel_2.setGeometry(QtCore.QRect(60, 90, 101, 21))
        self.deposit_amtLabel_2.setObjectName("deposit_amtLabel_2")
        self.login_pageButton_2 = QtWidgets.QPushButton(parent=self.savings)
        self.login_pageButton_2.setGeometry(QtCore.QRect(240, 300, 101, 21))
        self.login_pageButton_2.setStyleSheet("background-color: rgb(89, 78, 54);")
        self.login_pageButton_2.setObjectName("login_pageButton_2")
        self.deposit_inputEdit_2 = QtWidgets.QLineEdit(parent=self.savings)
        self.deposit_inputEdit_2.setGeometry(QtCore.QRect(180, 90, 113, 20))
        self.deposit_inputEdit_2.setStyleSheet("background-color: rgb(208, 221, 215);")
        self.deposit_inputEdit_2.setObjectName("deposit_inputEdit_2")
        self.savings_pageButton_2 = QtWidgets.QPushButton(parent=self.savings)
        self.savings_pageButton_2.setGeometry(QtCore.QRect(50, 300, 111, 21))
        self.savings_pageButton_2.setStyleSheet("background-color: rgb(89, 78, 54);")
        self.savings_pageButton_2.setObjectName("savings_pageButton_2")
        self.withdrawal_inputEdit_2 = QtWidgets.QLineEdit(parent=self.savings)
        self.withdrawal_inputEdit_2.setGeometry(QtCore.QRect(180, 180, 113, 20))
        self.withdrawal_inputEdit_2.setStyleSheet("background-color: rgb(208, 221, 215);")
        self.withdrawal_inputEdit_2.setObjectName("withdrawal_inputEdit_2")
        self.withdrawl_amtLabel_2 = QtWidgets.QLabel(parent=self.savings)
        self.withdrawl_amtLabel_2.setGeometry(QtCore.QRect(60, 180, 91, 20))
        self.withdrawl_amtLabel_2.setObjectName("withdrawl_amtLabel_2")
        self.action_requestLabel_2 = QtWidgets.QLabel(parent=self.savings)
        self.action_requestLabel_2.setGeometry(QtCore.QRect(40, 60, 271, 20))
        self.action_requestLabel_2.setObjectName("action_requestLabel_2")
        self.stackedWidget.addWidget(self.savings)
        self.welcome_Label = QtWidgets.QLabel(parent=self.centralwidget)
        self.welcome_Label.setGeometry(QtCore.QRect(100, 10, 161, 101))
        self.welcome_Label.setObjectName("welcome_Label")
        WelcomeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(WelcomeWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(WelcomeWindow)

    def retranslateUi(self, WelcomeWindow):
        _translate = QtCore.QCoreApplication.translate
        WelcomeWindow.setWindowTitle(_translate("WelcomeWindow", "MainWindow"))
        self.login_Label.setText(_translate("WelcomeWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Login with your name and four digit PIN</span></p></body></html>"))
        self.name_Label.setText(_translate("WelcomeWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Name:</span></p></body></html>"))
        self.PIN_Label.setText(_translate("WelcomeWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">PIN:</span></p></body></html>"))
        self.accountType_Label.setText(_translate("WelcomeWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Account Type:</span></p></body></html>"))
        self.checking_Radio.setText(_translate("WelcomeWindow", "Checking"))
        self.savings_Radio.setText(_translate("WelcomeWindow", "Savings"))
        self.login_button.setText(_translate("WelcomeWindow", "Login"))
        self.register_Label.setText(_translate("WelcomeWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Or, Register To Create an Account</span></p></body></html>"))
        self.register_button.setText(_translate("WelcomeWindow", "Register"))
        self.login_error_label.setText(_translate("WelcomeWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.register_error_label.setText(_translate("WelcomeWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.balance_Label.setText(_translate("WelcomeWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Your </span><span style=\" font-size:12pt; font-weight:600;\">checking</span><span style=\" font-size:12pt;\"> account balance is: </span></p></body></html>"))
        self.action_requestLabel.setText(_translate("WelcomeWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">What would you like to do?</span></p></body></html>"))
        self.deposit_amtLabel.setText(_translate("WelcomeWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Deposit Amount:</span></p></body></html>"))
        self.deposit_Button.setText(_translate("WelcomeWindow", "Deposit"))
        self.withdrawl_amtLabel.setText(_translate("WelcomeWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Withdrawal Amount:</span></p></body></html>"))
        self.withdrawal_Button.setText(_translate("WelcomeWindow", "Withdrawal"))
        self.statement_Button.setText(_translate("WelcomeWindow", "Checking Account Statement"))
        self.savings_pageButton.setText(_translate("WelcomeWindow", "Savings Account"))
        self.login_pageButton.setText(_translate("WelcomeWindow", "Return to Login"))
        self.balance_Label_2.setText(_translate("WelcomeWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Your </span><span style=\" font-size:12pt; font-weight:600;\">savings</span><span style=\" font-size:12pt;\"> account balance is: </span></p></body></html>"))
        self.statement_Button_2.setText(_translate("WelcomeWindow", "Savings Account Statement"))
        self.withdrawal_Button_2.setText(_translate("WelcomeWindow", "Withdrawal"))
        self.deposit_Button_2.setText(_translate("WelcomeWindow", "Deposit"))
        self.deposit_amtLabel_2.setText(_translate("WelcomeWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Deposit Amount:</span></p></body></html>"))
        self.login_pageButton_2.setText(_translate("WelcomeWindow", "Return to Login"))
        self.savings_pageButton_2.setText(_translate("WelcomeWindow", "Checking Account"))
        self.withdrawl_amtLabel_2.setText(_translate("WelcomeWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Withdrawal Amount:</span></p></body></html>"))
        self.action_requestLabel_2.setText(_translate("WelcomeWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">What would you like to do?</span></p></body></html>"))
        self.welcome_Label.setText(_translate("WelcomeWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Welcome to</span></p><p align=\"center\"><span style=\" font-size:14pt;\">World\'s Best Bank</span></p><p align=\"center\"><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WelcomeWindow = QtWidgets.QMainWindow()
    ui = Ui_WelcomeWindow()
    ui.setupUi(WelcomeWindow)
    WelcomeWindow.show()
    sys.exit(app.exec())