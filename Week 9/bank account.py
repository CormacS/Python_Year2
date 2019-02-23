class bankaccount():
    def __init__(self,account,balance):
        self.account = account
        self.balance = balance

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("insufficient funds")

x = bankaccount("125c",2000)
x.withdraw(200)

print(x.balance)