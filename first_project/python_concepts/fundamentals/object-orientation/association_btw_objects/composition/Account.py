import datetime
from BankStatement import BankStatement

class Account:
    def __init__(self, customers, number, balance):
        self.customers = customers
        self.number = number
        self.balance = balance
        self.opening_date = datetime.datetime.today()
        self.extract = BankStatement()

    def deposit(self, valor):
        self.balance += valor
        self.extract.transactions.append("done")

    def withdraw(self, valor):
       if self.balance < valor:
          return 'insufficient balance'
       else:
          self.balance -= valor
          self.extract.transactions.append("Withdraw: ", valor, "Date: ", datetime.datetime.today())

    def transfer(self, valor, account_to_transfer):
        if self.balance < valor:
            return 'insufficient balance'
        else:
            account_to_transfer.deposit(valor)
            self.balance -= valor
            self.extract.transactions.append("Transfer: ", valor, "Date: ", datetime.datetime.today())
            return 'done'

    def check_balance(self):
        print(f'Account: {self.number}\nCustomer: {self.customers}\nBalance: {self.balance}')

        #check the bug with datetime