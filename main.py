class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            return "Invalid deposit amount"
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount"
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

    def check_balance(self):
        return self.balance

new_account = Account("John Doe", 1000)
print(f"Balance: {new_account.check_balance()}")
print(f"Deposit: {new_account.deposit(500)}")
print(f"Withdraw: {new_account.withdraw(200)}")
print(f"Withdraw: {new_account.withdraw(1500)}")
print(f"Deposit: {new_account.deposit(-500)}")
print(f"Balance: {new_account.check_balance()}")