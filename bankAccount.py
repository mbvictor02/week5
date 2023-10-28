class BankAcc:
    # Base class for a simple bank account
    def __init__(self, account_number, balance=0):
        # Initialize the account with an account number and balance
        self.account_number = account_number
        self.balance = balance

    def get_account_details(self):
        # Retrieve account details including account number and balance
        return f"Account Number: {self.account_number}, Balance: {self.balance}"

    def deposit(self, amount):
        # Deposit funds into the account
        self.balance += amount

    def withdraw(self, amount):
        # Withdraw funds from the account if sufficient balance exists
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

class SavingsAccount(BankAcc):
    # Subclass inheriting from BankAcc for a savings account
    def __init__(self, account_number, balance=0, interest_rate=0):
        # Initialize the savings account with an interest rate
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def generate_interest(self):
        # Calculate and add interest to the account based on the balance and interest rate
        interest = self.balance * self.interest_rate
        self.balance += interest

    def change_interest_rate(self, new_rate):
        # Change the interest rate for the savings account
        self.interest_rate = new_rate

class CheckingAccount(BankAcc):
    # Subclass inheriting from BankAcc for a checking account
    def __init__(self, account_number, balance=0, transaction_fee=0):
        # Initialize the checking account with a transaction fee
        super().__init__(account_number, balance)
        self.transaction_fee = transaction_fee

    def withdraw(self, amount):
        # Withdraw funds, considering a transaction fee
        if self.balance >= amount + self.transaction_fee:
            self.balance -= amount + self.transaction_fee
        else:
            print("Insufficient funds.")
