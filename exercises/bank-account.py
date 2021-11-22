class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(self.name, "has been created with the balance of", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print(self.name, "balance has been updated with", amount)

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(self.name, "balance has been updated with", amount)

abi = Account('Abi', 1000)
abi
abi.deposit(500)
abi.withdraw(100)