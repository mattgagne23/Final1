from PyQt6.QtWidgets import *
from welcomeWindow import *
from checkingAccount import *
from savingAccount import *

class Account(QMainWindow, Ui_WelcomeWindow):
    VERIFIED = False #Will be used to check for login verification when accessing functions - class or function variable?

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        '''
        This function is used to initialize customer variables
        :param self.__account_name: Customer Name
        :param self.__account_ID: Customer PIN
        :param self.__account_balance: adjustable balance variable
        :param self.set_balance(self.__account_balance: this will set the balance object as the initial 0
        '''
        self.__account_name = name
        #self.__account_ID = special_Pin
        self.__account_balance = balance
        self.set_balance(self.__account_balance)

    def create_login(self, name, pin):
        '''
        Used with the register button to create record of account and initialize object. Will create, write,
        or read to global csv customer data file. Once added, name should be verified in varify_login function when logging in.
        :param self:
        :param name:
        :param pin:
        :return:
        '''

    def verify_login(self, name, pin):
        '''
        This function will verify the name and PIN combination entered against a file for validation.
        Should return True or False for validation. Will read a file for verification.
        '''

    def edit_account_file(self, name, pin):
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