# python oriented to object

# communication between objects

"""
a class has many objects instantiated in memory,
each one with its own attribute value.
To compare if two memory references point to the
same object, we use the signals "==" and "!=".
"""

class Account:
    def __init__(self, accountNumber, docNumber, name, balance):
        self.accountNumber = accountNumber
        self.docNumber = docNumber
        self.name = name
        self.balance = balance

    def deposit(self, value):
       self.balance += value

    def withdraw(self, value):
       if self.balance < value: #check if the account has balance
           return False
       else:
           self.balance -= value
           return True

    def bank_statement(self):
       print(f'Name: {self.name}\nAccount: {self.accountNumber}\nBalance: {self.balance}')

def main():
    account_1 = Account(2233, "13465467879", "Rafael Taparica", 0)
    account_2 = Account(3322, "57694837657", "Gabriela Bastos", 0)
    if (account_1 != account_2):
        print("different memory address")

    print(account_1)
    print(account_2)
    account_1.deposit(500)
    account_1.bank_statement()
    account_2.bank_statement()

#pointing the objects to the same memory address

    account_2 = account_1
    if (account_1 == account_2):
        print("The same memory address.")

    print(account_2)
    print(account_1)
    account_1.deposit(500)
    account_1.bank_statement()
    account_2.bank_statement()

if __name__ == "__main__":
    main()




