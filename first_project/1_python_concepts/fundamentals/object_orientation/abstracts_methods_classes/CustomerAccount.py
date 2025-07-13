from abc import ABC, abstractmethod

# abstract class and method
#abc (abstract base class), super class from abstract class

class CustomerAccount(ABC):
    def __init__(self, number, iof, ir, amount_invested, yield_rate):
        self.number = number
        self.iof = iof
        self.ir = ir
        self.amount_invested = amount_invested
        self.yield_rate = yield_rate

    #decorator @abstractmethod to indicate that the method is an abstract method
    @abstractmethod
    def performance_calculation(self):
        pass

    def extract(self):
        print(f"Account:  {self.number}\nBalance: {self.amount_invested}")

    