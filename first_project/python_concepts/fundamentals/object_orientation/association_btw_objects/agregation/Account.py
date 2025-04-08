f

class Account:
    def __init__(self, customers, number, balance):
        self.customers = customers
        self.number = number
        self.balance = balance

    def deposit(self, valor):
        self.balance += valor

    def withdraw(self, valor):
       if self.balance < valor:
          return 'insufficient balance'
       else:
          self.balance -= valor

    def transfer(self, valor, account_to_transfer):
        if self.balance < valor:
            return 'insufficient balance'
        else:
            account_to_transfer.deposit(valor)
            self.balance -= valor
            return 'done'

    def check_balance(self):
        print(f'Account: {self.number}\nCustomer: {self.customers}\nBalance: {self.balance}')