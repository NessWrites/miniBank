from accounts import SavingAccount, CheckingAccount
from transactions import perform_transaction


def main():
    #Creating instances of different account types
    savings = SavingAccount("001", "LonelyNess", 0.03)
    checking = CheckingAccount("002", "SadNess", 500)


    #Performing transactions
    perform_transaction(savings, 'deposit', 1000)
    perform_transaction(checking, 'deposit', 500)
    perform_transaction(savings, 'withdraw', 200)
    perform_transaction(checking, 'withdraw', 700)

	# Adding interest to savings account
    savings.add_interest()

    # Checking balances
    print(f"Savings Account Balance: {savings.check_balance()}")
    print(f"Checking Account Balance: {checking.check_balance()}")

if __name__ == "__main__":
    main()