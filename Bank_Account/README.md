# Bank Account Class in Python

## Problem Statement

 Create a Python class called BankAccount with the following methods:


```__init__(self, owner, balance)```: Initialize the BankAccount object with the owner's name (a string) and the initial balance (a float).

```deposit(self, amount):``` Add the given amount to the account's balance.

```withdraw(self, amount):``` Deduct the given amount from the account's balance. Ensure that the account balance doesn't go below zero. If there are insufficient funds, print an error message.

```get_balance(self):``` Return the current balance of the account.

Now, write a solution to implement the BankAccount class and test it with some example transactions.

## Example Usage

```python
# Create BankAccount objects
p1 = BankAccount("Shashank", 1000)
p2 = BankAccount("baymax", 500)
p3 = BankAccount("harry", 900)

# Deposit money
print(p1.deposit(500))  # Output: "You've deposited 500 & your new balance is 1500"

# Get balance
print(p1.get_balance())  # Output: "Your balance is 1500"

# Withdraw money
print(p1.withdraw(4000))  # Output: "Invalid withdrawal request of amount 4000, your account has 1500"
```

