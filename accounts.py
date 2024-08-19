"""
 
 banking_system/
│
├── accounts.py       # Contains the class: BankAccount(deposit, withdrawl), class: SavingsAccount(adds interest), and class: CheckingAccount() 
├── transactions.py   # Contains transaction-related classes or functions
├── main.py           # The main script to run the project
└── __init__.py       # Makes this directory a package
 
 
	"""

class BankAccount:
    def __init__(self, account_number, account_holder):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = 0.00

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Deposited Balance: {amount}. You have now {self.__balance} at your bank account')
        else:
            print('Invalid deposit amount')

    def withdraw(self, amount):
        if self.__balance > amount > 0:
            self.__balance -= amount
            print(f'Withdrawn Amount: {amount}. You have now {self.__balance} at your bank account')
        else:
            print('Invalid withdrawn amount')

    def check_balance(self):
        return self.__balance
    
    def get_accountholder(self):
        return self.__account_holder




class SavingAccount:
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate
        
    def add_interest(self):
        interest = self.interest_rate * self.check_balance()
        self.depost(interest)
        print(f"Interest added: {interest}. New balance is {self.check_balance()}.")




class CheckingAccount:
    def __init__(self, account_number, account_holder, overdraft_limit):
        super().__init__(account_number, account_holder)
        self.overdraft_limit = overdraft_limit

#there is withdraw method in bank accout too.. Polymor
    def withdraw(self, amount):
        if amount<= self.check_balance() + self.overdraft_limit:
            self._BankAccount__balance -= amount
            print(f'Withdrew {amount}. New balance is {self.check_balance()}.')
        else:
            print('Exceeded overdraft limit')
            

"""Polymorphism:
The withdraw method is overridden in CheckingAccount to accommodate the overdraft feature,

 demonstrating polymorphism. Both SavingsAccount and CheckingAccount can be used interchangeably where BankAccount is expected.
		"""
            