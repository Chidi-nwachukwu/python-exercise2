class Account:
    def _init_(self, account_number, balance):
        self.balance = balance
        self.account_number = account_number

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def __str__(self):
        return f"Account is{self.balance}, "


chidiebere_gt_acct = Account("12345667")
print(chidiebere_gt_acct)
