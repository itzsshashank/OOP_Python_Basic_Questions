class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"You've deposited {amount} & your new balance is {self.balance}"
        else:
            return "Invalid Deposit amount"

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance or withdraw_amount < 0:
            return f"Invalid withdrawal request of amount {withdraw_amount}, your account has {self.balance}"
        elif withdraw_amount > 0 or withdraw_amount < self.balance:
             self.balance = self.balance - withdraw_amount
             return f"You withdrew {withdraw_amount} and you're left with {self.balance}"

    def get_balance(self):
        return f"Your balance is {self.balance}"


p1 = BankAccount("Shashank", 1000)
p2 = BankAccount("baymax", 500)
p3 = BankAccount("harry", 900)


# Example
print(p1.deposit(500))
print(p1.get_balance())
print(p1.withdraw(4000))
print(p1.get_balance())
print(p1.deposit(120))
