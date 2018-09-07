class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return ("Account owner: " + str(self.owner)) + "\n" + ("Account balance: $" + str(self.balance))

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Withdrawal cannot be processed. Not enough money, your current balance is: " + str(self.balance))
        else:
            self.balance -= amount
            print('Withdrawal processed successfully. Your current balance is: ' + str(self.balance))


jose_account = Account("Jose", 5000)
print(jose_account)
print(jose_account.balance)
print(jose_account.owner)
jose_account.deposit(500)
print(jose_account)
jose_account.withdrawal(4010)
