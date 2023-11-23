class Bank:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    # this is also the last question i combined it into one func
    def holders_data(self):
        print(f"account number: {self.account_number}, account holder: {self.account_holder}, initial balance: {self.balance}")

    def deposit(self, money_added):
        self.balance += money_added
        return money_added

    def withdraw(self, money_lost):
        if money_lost > self.balance:
            return "you dont' have that much money"
        else:
            self.balance -= money_lost
            return self.balance


account = Bank(113567, "Alon", 27)
account.holders_data()
account.deposit(5)
account.withdraw(20)
account.withdraw(28)
account.holders_data()