import random

class Account():
    Account_count = 0

    def __init__(self, username, balance):
        self.username = username
        self.balance = balance
        self.bankname = "SC은행"
        num1 = str(random.randint(0, 999)).zfill(3)
        num2 = str(random.randint(0, 99)).zfill(2)
        num3 = str(random.randint(0,999999)).zfill(6)
        self.accNo = num1 + '-' + num2 + '-' + num3
        Account.Account_count += 1

John = Account("John", 1000)
print(Account.Account_count)