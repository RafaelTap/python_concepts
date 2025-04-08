from math import acosh

from Account import Account
import datetime

class SpecialAccount(Account): # in java: extends ...
    def __init__(self, customer, number, balance, limit):
        super().__init__(customer, number , balance) # the superclass constructor
        self.limit = limit #exclusive attribute

    #polymorphism of withdraw method from class Account
    def withdraw(self, value):
        if (self.balance + self.limit < value):
            print("No balance")
            return False #when the condition is true, we use "return False".
        else:
            self.balance -= value
            if (self.balance < 0):
                self.limit += self.balance
            self.extract.transactions.append("Balance: ", {self.balance})
            return True

        def deposit(self, value):
            pass



