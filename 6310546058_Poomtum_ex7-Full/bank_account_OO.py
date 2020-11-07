import random


class Account:
    def __init__(self, name):
        self.account_ID = str(random.randint(1000, 9999))
        self.account_name = 'account' + str(name)
        self.balance = random.randint(20, 2000)

    def __str__(self):
        return "{0}:{1}".format(self.account_ID, [self.account_name, self.balance])


class Database:
    def __init__(self):
        self.bank_account_DB = {}

    def add_account(self, account):
        self.bank_account_DB[account.account_ID] = [account.account_name, account.balance]

    def search(self, ID):
        if ID in self.bank_account_DB.keys():
            return True
        else:
            return False

    def deposit(self, ID, amount):
        if self.search(ID):
            self.bank_account_DB[ID][1] += amount
        else:
            print('Record not found.')

    def withdraw(self, ID, amount):
        if not self.search(ID):
            print('Record not found.')
        else:
            if self.bank_account_DB[ID][1] < amount:
                print('Insufficient funds. Transaction aborted.')
            else:
                self.bank_account_DB[ID][1] -= amount

    def __str__(self):
        return "\n".join([i + ':' + str(self.bank_account_DB[i]) for i in self.bank_account_DB])


d = Database()

# generate 10 random bank accounts and put them in the bank account database, bank_account_DB
for i in range(10):
    d.add_account(Account(i))

# main loop to run our banking system
while True:
    print('Banking System Menu:')
    print('Press 1 to display all records.')
    print('Press 2 to search for a record')
    print('Press 3 to deposit amount')
    print('Press 4 to withdraw amount')
    print('Press 0 to exit')
    choice = input('Enter a choice (0-4): ')
    if choice == '0':
        break
    elif choice == '1':
        print(d)
    elif choice == '2':
        search_account = input('Enter an account number to search: ')
        if d.search(search_account):
            print(search_account + ':' + str(d.bank_account_DB[search_account]))
        else:
            print('Record not found.')
    elif choice == '3':
        deposit_account = input('Enter an account number to deposit: ')
        deposit_amount = float(input('Enter an amount to deposit: '))
        d.deposit(deposit_account, deposit_amount)
    elif choice == '4':
        withdraw_account = input('Enter an account number to withdraw: ')
        withdraw_amount = float(input('Enter an amount to withdraw: '))
        d.withdraw(withdraw_account, withdraw_amount)
    else:
        print('Invalid choice selection. Please try again')