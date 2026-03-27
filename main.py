class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def validate_deposit(self, amount):
        if amount < 0:
            print("Invalid deposit amount")
            return False
        return True
    

new_account = Account("John Doe", 1000)
new_account.check_balance()
new_account.deposit(500)
new_account.withdraw(200)
new_account.withdraw(1500)
new_account.validate_deposit(-100)