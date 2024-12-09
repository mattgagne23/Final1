from multiprocessing.managers import Value

from PyQt6.QtWidgets import *
from welcomeWindow import *
from checkingAccount import *
from savingAccount import *
import csv
import os.path

class Account(QMainWindow, Ui_WelcomeWindow, Ui_checkingAccount, Ui_savingsAccount):
    VERIFIED = False #Will be used to check for login verification when accessing functions - class or function variable?

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.register_button.clicked.connect(lambda : self.register_button_clicked())
        self.login_button.clicked.connect(lambda : self.login_button_clicked())

        '''
        This function is used to initialize customer variables
        :param self.__account_name: Customer Name
        :param self.__account_ID: Customer PIN
        :param self.__account_balance: adjustable balance variable
        :param self.set_balance(self.__account_balance: this will set the balance object as the initial 0
        '''
        #self.__account_name = name
        #self.__account_ID = special_Pin
        #self.__account_balance = balance
        #self.set_balance(self.__account_balance)

    def register_button_clicked(self):
        '''
        Used with the register button to create record of account and initialize object. Will create, write,
        or read to global csv customer data file. Once added, name should be verified in varify_login function when logging in.
        :param self:
        :param already_registered: Used to show if user is already registered
        :param name: Name entered
        :param PIN: PIN entered
        :param login_data: Used to store list of Name, PIN
        :param path: Used to store file path
        :return:
        '''
        already_registered = False
        path = './login_list.csv'
        name = self.name_Edit.text().strip()
        PIN = self.PIN_Edit.text().strip()

        try:
            if name == '':
                raise ValueError
            if PIN == '':
                raise ValueError
            if len(PIN) != 4:
                raise ValueError
        except ValueError:
            self.register_error_label.setText('Enter a valid Name and PIN')
        else:

            login_data = [name, PIN]

            if os.path.isfile(path) == False:
                with open('login_list.csv', 'w', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerow(['Name', 'PIN'])

            with open('login_list.csv', 'r', newline='') as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    if row == login_data:
                        self.register_error_label.setText('Account already exists')
                        already_registered = True

            if already_registered == False:
                with open('login_list.csv', 'a', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerow(login_data)
                    self.register_error_label.setText('Account has been created!')
                with open(f'checking_{name}_{PIN}.csv', 'w', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerow(['CHECKING', name, PIN])
                with open(f'savings_{name}_{PIN}.csv', 'w', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerow(['SAVINGS', name, PIN])

            self.name_Edit.clear()
            self.PIN_Edit.clear()
            self.login_error_label.setText('')
            self.account_selection_label.setText('')

    def login_button_clicked(self):
        '''
        This function will verify the name and PIN combination entered against a file for validation.
        Should return True or False for validation. Will read a file for verification.
        '''
        already_registered = False
        path = './login_list.csv'
        name = self.name_Edit.text().strip()
        PIN = self.PIN_Edit.text().strip()

        if self.checking_Radio.isChecked():
            account = 'checking'
        elif self.savings_Radio.isChecked():
            account = 'savings'
        else:
            self.account_selection_label.setText('You must choose an account!')

        try:
            if name == '':
                raise ValueError
            if PIN == '':
                raise ValueError
            if len(PIN) != 4:
                raise ValueError
        except ValueError:
            self.register_error_label.setText('Enter a valid Name and PIN')
        else:

            login_data = [name, PIN]

            if os.path.isfile(path) == False:
                self.login_error_label.setText('No registered users!')

            else:
                with open('login_list.csv', 'r', newline='') as csvfile:
                    csv_reader = csv.reader(csvfile)
                    for row in csv_reader:
                        if row == login_data:
                            ###LOGIC TO CHANGE TO CHECKING OR SAVINGS WINDOW BASED ON RADIO BUTTON
                            self.login_error_label.setText('Account already exists')
                            already_registered = True

                if already_registered == False:
                    self.login_error_label.setText('You must register to create a bank account!')

            self.name_Edit.clear()
            self.PIN_Edit.clear()
            self.register_error_label.setText('')

    def edit_account_file(self):
        '''
        Used to either create, write, or read transaction data to applicable account. Maybe have an option to clear.
        If an account file does not exist for a customer, create csv file with format name_pin to locate upon re-logging
        in.
        :param self:
        :param name:
        :param pin:
        :return:
        '''

    def deposit(self, amount):
        '''
        This function is used to add a valid amount to a balance.
        This would need to be recorded in the account transaction file as a credit, and needs to work with balance
        variable in file.
        :param self.__account_balance: This is the variable funds would be added to
        :param amount: Amount to be added to account balance that must be greater than 0
        :return:
        '''
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount):
        '''
        Similar function to deposit, will reduce balance by a valid amount. Will record in account file. Needs to be
        recorded as a debit in transaction file, needs to use balance stored in file.
        Amount cannot be less than 1 or more than entire balance.
        '''
        if (amount <= 0) or (amount > self.__account_balance):
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self):
        '''
        Used to retrieve balance amount from file. Might be tricky but should be able to save final balance to top row?
        :param self:
        :return:
        '''
        return self.__account_balance

    def get_name(self):
        '''
        Return account name currently being used. Will be used for account screens after login.
        :param self:
        :return:
        '''
        return self.__account_name

    def set_balance(self, value):
        '''
        Would be used in conjunction with withdraw and deposit. Potentially have the account file balance updated
        here.
        :param self:
        :param value:
        :return:
        '''
        if value < 0:
            self.__account_balance = 0
        else:
            self.__account_balance = value

    def set_name(self, value):
        '''
        Not sure if this will be used. Might be needed during global variable process but might be consolidated
        with create login.
        :param self:
        :param value:
        :return:
        '''
        self.__account_name = value

    def __str__(self):
        '''
        Need to change, but should be able to print things like:
        "Welcome, {name}!"
        "Your {account_type} balance is: {account balance}"
        :param self:
        :return:
        '''
        return f'Account name = {self.get_name()}, Account balance = {self.get_balance():.2f}'

class SavingAccount(Account):
    '''
    This class is to use inheritance and create another object for a savings account that has calculated interest.
    This will be adjusted accordingly with functions being changed above.
    '''
    minimum = 100
    rate = 0.02

    def __init__(self, name):
        super().__init__(name, SavingAccount.minimum)
        self.__deposit_count = 0

    def apply_interest(self):
        if self.__deposit_count % 5 == 0:
            self.set_balance(self.get_balance() + (self.get_balance() * SavingAccount.rate))

    def deposit(self, amount):
        if amount <= 0:
            return False
        else:
            self.set_balance(self.get_balance() + amount)
            self.__deposit_count += 1
            self.apply_interest()
            return True

    def withdraw(self, amount):
        if (amount <= 0) or ((self.get_balance() - amount) < SavingAccount.minimum):
            return False
        else:
            self.set_balance(self.get_balance() - amount)
            return True

    def set_balance(self, value):
        if value < SavingAccount.minimum:
            super().set_balance(SavingAccount.minimum)
        else:
            super().set_balance(value)

    def set_name(self, value):
        super().set_name(value)

    def __str__(self):
        return f'SAVING ACCOUNT: {super().__str__()}'