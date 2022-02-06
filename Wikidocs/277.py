import random

class Account():
    Account_count = 0
    Deposit_count = 0

    def __init__(self, username, balance):
        self.username = username
        self.balance = balance
        self.bankname = "SC은행"
        num1 = str(random.randint(0, 999)).zfill(3)
        num2 = str(random.randint(0, 99)).zfill(2)
        num3 = str(random.randint(0,999999)).zfill(6)
        self.accNo = num1 + '-' + num2 + '-' + num3
        Account.Account_count += 1

    def get_account_num():
        print(Account.Account_count)

    def deposit(self, amount):
        if amount < 1:
            print("Deposit must be over 1.")

        else:
            self.balance += amount
            Account.Deposit_count += 1
            print(f"Deposit amount: {amount}.\n Total balance: {self.balance}")
            if Account.Deposit_count % 5 == 0:
                self.balance = self.balance * 1.01

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount must be lower than current balance.")
        else:
            self.balance -= amount
            print(f"Withdrawal amount: {amount}.\n Total balance: {self.balance}")

    def display_info(self):
        print(f"은행이름: {self.bankname}")
        print(f"예금주: {self.username}")
        print(f"계좌번호: {self.accNo}")
        print(f"잔고: {self.balance:,}원")

John = Account("John", 1000)
John.deposit(1000)
John.deposit(1000)
John.deposit(1000)
John.deposit(1000)
John.deposit(1000)
John.display_info()