from multiprocessing.managers import Value

from PyQt6.QtWidgets import *
from mainWindow import *
import csv
import os.path

class Account(QMainWindow, Ui_WelcomeWindow):

    def __init__(self, name='', pin=''):
        '''
        Function to initialize window and first stackable widget page. Also houses
        button clicking relationships.
        '''
        super().__init__()
        self.setupUi(self)

        self.__name = name
        self.__pin = pin

        self.register_button.clicked.connect(lambda : self.register_button_clicked())
        self.login_button.clicked.connect(lambda : self.login_button_clicked())
        self.deposit_Button.clicked.connect(lambda: self.deposit())
        self.withdrawal_Button.clicked.connect(lambda: self.withdraw())
        self.deposit_Button_2.clicked.connect(lambda: self.deposit_savings()) #savings deposit
        self.withdrawal_Button_2.clicked.connect(lambda: self.withdraw_savings()) #savings withdrawal

        self.savings_pageButton.clicked.connect(lambda : self.show_savings())
        self.checking_pageButton.clicked.connect(lambda : self.show_checking())
        self.login_pageButton.clicked.connect(lambda : self.show_login())
        self.login_pageButton_2.clicked.connect(lambda : self.show_login()) #savings login return

        self.stackedWidget.setCurrentWidget(self.welcome)

        '''
        This function is used to initialize customer variables
        :param self.__account_name: Customer Name
        :param self.__account_ID: Customer PIN
        :param self.__account_balance: adjustable balance variable
        :param self.set_balance(self.__account_balance: this will set the balance object as the initial 0
        '''

    def show_checking(self):
        '''
        This function is used to change the stackable widget page to checking page and grabs current balance.
        '''
        balance = self.get_checking_balance()
        self.stackedWidget.setCurrentWidget(self.checking)
        self.balance_Label.setText(f'Your checking balance is {balance:.2f}')

    def show_savings(self):
        '''
        This function is used to change the stackable widget page to savings page and grabs current balance.
        '''
        balance = self.get_savings_balance()
        self.stackedWidget.setCurrentWidget(self.savings)
        self.balance_Label_2.setText(f'Your savings balance is {balance:.2f}')

    def show_login(self):
        '''
        This function is used to change the stackable widget page to login screen.
        '''
        self.stackedWidget.setCurrentWidget(self.welcome)

    def register_button_clicked(self):
        '''
        Used with the register button to create record of account. Will create, write,
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
        self.__name = self.name_Edit.text().strip()
        self.__pin = self.PIN_Edit.text().strip()

        try:
            if self.__name == '':
                raise ValueError
            if self.__pin == '':
                raise ValueError
            if len(self.__pin) != 4:
                raise ValueError
        except ValueError:
            self.register_error_label.setText('Enter a valid Name and PIN')
        else:

            login_data = [self.__name, self.__pin]

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
                with open(f'checking_{self.__name}_{self.__pin}.csv', 'w', newline='') as csvfile:
                    pass
                with open(f'savings_{self.__name}_{self.__pin}.csv', 'w', newline='') as csvfile:
                    pass

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
        self.__name = self.name_Edit.text().strip()
        self.__pin = self.PIN_Edit.text().strip()

        if self.checking_Radio.isChecked():
            account = 'checking'
        elif self.savings_Radio.isChecked():
            account = 'savings'
        else:
            self.account_selection_label.setText('You must choose an account!')

        try:
            if self.__name == '':
                raise ValueError
            if self.__pin == '':
                raise ValueError
            if len(self.__pin) != 4:
                raise ValueError
        except ValueError:
            self.register_error_label.setText('Enter a valid Name and PIN')
        else:

            login_data = [self.__name, self.__pin]

            if os.path.isfile(path) == False:
                self.login_error_label.setText('No registered users!')

            else:
                with open('login_list.csv', 'r', newline='') as csvfile:
                    csv_reader = csv.reader(csvfile)
                    for row in csv_reader:
                        if row == login_data:
                            #LOGIC TO CHANGE TO CHECKING OR SAVINGS WINDOW BASED ON RADIO BUTTON
                            #self.login_error_label.setText('Account already exists')
                            already_registered = True

                if already_registered == True:
                    if self.checking_Radio.isChecked():
                        self.show_checking()
                    elif self.savings_Radio.isChecked():
                        self.show_savings()
                    else:
                        self.account_selection_label.setText('You must choose an account!')

                if already_registered == False:
                    self.login_error_label.setText('You must register to create a bank account!')

            self.name_Edit.clear()
            self.PIN_Edit.clear()
            self.register_error_label.setText('')

    def get_checking_balance(self):
        '''
        This function has the purpose of reading through the applicable csv file
        and returning the balance total.
        :return: Returns the balance calculated from the rows in csv file.
        '''
        balance = 0
        with open(f'checking_{self.__name}_{self.__pin}.csv', 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                for value in row:
                    balance += float(value)

        return balance

    def get_savings_balance(self):
        '''
        This function has the purpose of reading through the applicable savings csv file and returning the balance total.
        :return: Returns the balance calculated from the rows in csv file.
        '''
        balance = 0
        with open(f'savings_{self.__name}_{self.__pin}.csv', 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                for value in row:
                    balance += float(value)

            return balance

    def deposit(self):
        '''
        This function is used to add a valid amount to a balance.
        This would need to be recorded in the account transaction file as a credit, and needs to work with balance
        variable in file.
        :param amount: Amount to be added to account balance that must be greater than 0
        '''

        try:
            amount = float(self.deposit_inputEdit.text().strip())
            if amount == '':
                raise TypeError
            if float(amount) <= 0:
                raise TypeError
        except ValueError:
            self.deposit_error.setText('Values must be numeric')
        except TypeError:
            self.deposit_error.setText('Deposit must be greater than 0')
        else:
            amount = (f'{amount:.2f}')
            with open(f'checking_{self.__name}_{self.__pin}.csv', 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([amount])

            balance = self.get_checking_balance()

            self.balance_Label.setText(f'Your checking account balance is {balance:.2f}')

            self.deposit_inputEdit.clear()

    def withdraw(self):
        '''
        Similar function to deposit, will reduce balance by a valid amount. Will record in account file. Needs to be
        recorded as a debit in transaction file, needs to use balance stored in file.
        Amount cannot be less than 1 or more than entire balance.
        :param initial_balance: used to check amount against balance
        '''
        initial_balance = self.get_checking_balance()

        try:
            amount = float(self.withdrawal_inputEdit.text().strip())
            if amount == '':
                raise TypeError
            if float(amount) <= 0:
                raise TypeError
            if float(amount) > initial_balance:
                raise TypeError
        except ValueError:
            self.withdrawal_error.setText('Values must be numeric')
        except TypeError:
            self.withdrawal_error.setText('Please enter valid withdrawal amount')
        else:
            amount = (f'-{amount:.2f}')
            with open(f'checking_{self.__name}_{self.__pin}.csv', 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([amount])

            balance = self.get_checking_balance()

            self.balance_Label.setText(f'Your checking account balance is {balance:.2f}')

            self.withdrawal_inputEdit.clear()

    def deposit_savings(self):
        '''
        This function is used to deposit funds into savings account.
        :param amount: Amount being deposited that must be greater than 0 and must be numeric
        '''

        rate = 0.02

        try:
            amount = float(self.deposit_inputEdit_2.text().strip())
            if amount == '':
                raise TypeError
            if float(amount) <= 0:
                raise TypeError
        except ValueError:
            self.deposit_error_2.setText('Values must be numeric')
        except TypeError:
            self.deposit_error_2.setText('Deposit must be greater than 0')
        else:
            interest = amount * rate
            amount_with_interest = interest + amount
            amount_with_interest = (f'{amount_with_interest:.2f}')
            with open(f'savings_{self.__name}_{self.__pin}.csv', 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([amount_with_interest])

            balance = self.get_savings_balance()

            self.balance_Label_2.setText(f'Your checking account balance is {balance:.2f}')

            self.deposit_inputEdit_2.clear()

    def withdraw_savings(self):
        '''
        This is a function to withdraw funds from the savings account.
        :param amount: The amount entered to be withdrawn. This cannot be less than 0 or greater than account balance.
        '''
        initial_balance = self.get_savings_balance()

        try:
            amount = float(self.withdrawal_inputEdit_2.text().strip())
            if amount == '':
                raise TypeError
            if float(amount) <= 0:
                raise TypeError
            if float(amount) > initial_balance:
                raise TypeError
        except ValueError:
            self.withdrawal_error_2.setText('Values must be numeric')
        except TypeError:
            self.withdrawal_error_2.setText('Please enter valid withdrawal amount')
        else:
            amount = (f'-{amount:.2f}')
            with open(f'savings_{self.__name}_{self.__pin}.csv', 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([amount])

            balance = self.get_savings_balance()

            self.balance_Label_2.setText(f'Your checking account balance is {balance:.2f}')

            self.withdrawal_inputEdit_2.clear()
