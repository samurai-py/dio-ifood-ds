# account.py

class Account:
    account_number = 1

    def __init__(self, user):
        self.branch = '0001'
        self.number = Account.account_number
        Account.account_number += 1
        self.user = user
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
