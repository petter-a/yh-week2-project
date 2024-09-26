class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount: float):
        self.balance += amount
    
    def withdraw(self, amount: float):
        result = self.balance - amount
        if result >= 0:
            self.balance = result            
        
    def display_balance(self):
        print(f"{self.owner}: {self.balance}")

def main():
    account = BankAccount('myaccount')

    account.display_balance() # = 0
    account.deposit(100)
    account.deposit(25.50)
    account.display_balance() # = 125.5
    account.withdraw(50)
    account.display_balance() # = 75.5
    account.withdraw(100)
    account.display_balance() # = 75.5

main()