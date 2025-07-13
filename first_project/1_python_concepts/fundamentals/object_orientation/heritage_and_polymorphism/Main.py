from Customer import Customer
from Account import Account
from SpecialAccount import SpecialAccount

ac_3 = SpecialAccount("Rafael Taparica", 4455, 1000, 800)

#balance print
print(f'Balance: {ac_3.balance}\nCredit Limt: {ac_3.limit}')

#withdraw
ac_3.withdraw(500)
print(f'Balance: {ac_3.balance}\nCredit Limt: {ac_3.limit}')
