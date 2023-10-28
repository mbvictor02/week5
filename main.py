from BankAccount import BankAcc, SavingsAccount, CheckingAccount

current_account = None  # Variable to store the currently selected account

# Function to create a new account
def create_account():
    global current_account  # Access the global variable to store the current account
    print("What type of account would you like to create? (1 - Bank Account, 2 - Savings Account, 3 - Checking Account)")
    choice = input("Enter your choice: ")

    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))

    # Create a new account based on user choice and account details
    if choice == "1":
        current_account = BankAcc(account_number, initial_balance)
        print("Bank Account created.")
    elif choice == "2":
        interest_rate = float(input("Enter interest rate for the Savings Account: "))
        current_account = SavingsAccount(account_number, initial_balance, interest_rate)
        print("Savings Account created.")
    elif choice == "3":
        transaction_fee = float(input("Enter transaction fee for the Checking Account: "))
        current_account = CheckingAccount(account_number, initial_balance, transaction_fee)
        print("Checking Account created.")
    else:
        print("Invalid choice. Please try again.")
        create_account()  # If the choice is invalid, restart the account creation process

# Function displaying the main menu for account operations
def main_menu():
    print("\nMain Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Get Account Details")
    print("4. Change Interest Rate/Transaction Fee (Savings/Checking Account)")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Perform actions based on user choice
    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        current_account.deposit(amount)
        print("Deposit successful.")
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        current_account.withdraw(amount)
    elif choice == "3":
        details = current_account.get_account_details()
        print(details)
    elif choice == "4":
        # Check the account type and allow modifying interest rate or transaction fee accordingly
        if isinstance(current_account, SavingsAccount):
            new_interest_rate = float(input("Enter new interest rate: "))
            current_account.change_interest_rate(new_interest_rate)
            print("Interest rate changed.")
        elif isinstance(current_account, CheckingAccount):
            new_transaction_fee = float(input("Enter new transaction fee: "))
            current_account.transaction_fee = new_transaction_fee
            print("Transaction fee changed.")
        else:
            print("This operation is not available for Bank Accounts.")
    elif choice == "5":
        print("Thank you for using the UAX Bank. Goodbye!")
        exit()  # Terminate the program when the user chooses to exit
    else:
        print("Invalid choice. Please try again.")

    main_menu()  # Display the main menu again after an action is performed

# Chatbot starts here
print("Welcome to the UAX Bank!")
create_account()  # Create an initial account
main_menu()  # Display the main menu for operations
