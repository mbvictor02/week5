class BankAcc:
    def __init__(self, account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance
    
    def get_account_number(self):
        return self.account_number
    
    def get_balance(self):
        return self.balance
    
    def deposit(self, deposit):
        self.balance += deposit
    
    def withdraw(self, withdraw):
        self.balance -= withdraw
    
    #def __str__(self):

class SavingsAccount(BankAcc):
    def __init__(interest_rate,interests_generated):
        super().__init__(interest_rate,interests_generated)

class CheckingAccount(BankAcc):
    def __init__(overdraft_limit):
        super().__init__(overdraft_limit)

bank_account1 = BankAcc("ES9898989898", 10)
bank_account1.deposit(5)
print(f"The account {bank_account1.get_account_number()} has {bank_account1.get_balance()}") 

#IMPORTANTE = entrara definicion del OPP