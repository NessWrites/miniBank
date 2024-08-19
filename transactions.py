from accounts import BankAccount, SavingAccount, CheckingAccount

def perform_transaction(account, transaction_type, amount):
    if transaction_type == 'deposit':
        account.deposit(amount)
    elif transaction_type =='withdraw':
        account.withdraw(amount)
    else:
        print("Invalid transaction type.")