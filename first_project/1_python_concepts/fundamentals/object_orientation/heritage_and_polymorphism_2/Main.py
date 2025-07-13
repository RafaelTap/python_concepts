from Bank import Bank
from CustomerAccount import CustomerAccount
from PaidAccount import PaidAccount
from CommonAccount import CommonAccount

bank_1 = Bank("Money Bank", 2233)
customer_account_1 = CustomerAccount(3344, 0.05, 0.1, 2000, 400)
paid_account_1 = PaidAccount(4455, 0.04, 0.08, 1000, 200)
common_account_1 = CommonAccount(5566, 0.05, 0.07, 1500, 350)

bank_1.add_account(customer_account_1)
bank_1.add_account(paid_account_1)
bank_1.add_account(common_account_1)

bank_1.month_performance()
bank_1.print_balance()
