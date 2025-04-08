from Account import Account
from Customer import Customer

c_1 = Customer("rafael taparica", "18467309784")
c_2 = Customer("Gabriela", "57664912937")

a_1 = Account([c_1.name, c_2.name], 3456, 3456.55)

a_1.check_balance()
a_1.deposit(2000)
a_1.withdraw(345)
a_1.check_balance()