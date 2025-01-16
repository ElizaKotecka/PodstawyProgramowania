class Bank:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0

    def deposit(self):
        amount = float(input('Please, enter an aomunt to deposit: '))
        self.balance += (amount)
        print(f'{amount:.2f} PLN successfully deposited.')

    def withdraw(self):
        amount = float(input('Please, enter an aomunt to withdraw: '))
        if amount > self.balance:
            print("Insufficient funds on the account.")
        else:
            self.balance -= amount
            print(f'Issuing money from an ATM... \n{amount:.2f} PLN successfully withdraw.')
        
    def display(self):
        print(f'Bank Account No: {self.account_number} \nBalance: PLN {self.balance:.2f}')