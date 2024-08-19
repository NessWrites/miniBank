from accounts import SavingAccount, CheckingAccount
from transactions import perform_transaction


def main():
    #Creating instances of different account types
    savings = SavingAccount("001", "LonelyNess", 0.03)
    """
    Here, super().__init__(account_number, account_holder) ensures that savings.__account_number 
    and savings.__account_holder are properly initialized by the BankAccount class, while 
    self.interest_rate = interest_rate sets the interest rate specifically for the SavingsAccount class.
    
    When you create an instance of SavingsAccount, its __init__ method is called.
    
    super().__init__(account_number, account_holder) is used to initialize the attributes inherited from BankAccount.
    
	After the parent class’s __init__ is called, the SavingsAccount class can initialize its own attributes, like interest_rate.
 
 
    When you create a SavingsAccount object, both the BankAccount and SavingsAccount constructors are executed, ensuring that the 
    object is fully initialized with all necessary attributes from both classes.
	"""
    
    
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