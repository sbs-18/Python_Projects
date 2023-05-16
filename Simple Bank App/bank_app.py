import math

class Account:
    def __init__(self,initial_amount = 0.00):
        self.balance = initial_amount
     
    def Check_Balance(self):
        print("Your current balance :",self.balance)

    def Withdrawal(self, amount):
        if(amount > self.balance):
            print("Can't withdraw, Your current balance is :",self.balance)
            return
        if amount >= 1:
            self.balance = self.balance - amount
            print("Amount withdrew : ",amount)
            print("Your current balance : ",self.balance)
            self.transaction_history(f"Withdrew :{amount}")
        else:
            print("Invalid amount,Try again")
    
    def Deposit(self, amount):
        if amount >= 1:
            self.balance = self.balance + amount
            print("Amount Deposited : ",amount)
            print("Your current balance : ",self.balance)
            self.transaction_history(f"Deposited :{amount}")
        else:
            print("Invalid amount,try again")

    def transaction_history(self, transactions):
        with open("transactions.txt",'a') as file:
            file.write(f"{transactions}\t\t\t Balance: {self.balance}\n")


account = Account(50)

while True:
    while True:
        print("\n1.Withdraw\n2.Deposit\n3.Check Balance\n4.Exit\n")
        action = input("Choose your action : ")
        try:
            action = int(action)
            break
        except Exception:
            print("Error : Invalid Option")

    if action in range(1,5):
        if action==1:
            amount = input("Enter the amount you want to withdraw : ")
            try:
                amount = float(amount)
                amount = math.floor(amount)
                account.Withdrawal(amount)
            except Exception:
                print("Invalid amount,try again")

        elif action==2:
            amount = input("Enter the amount you want to deposit : ")
            try:
                amount = float(amount)
                amount = math.floor(amount)
                account.Deposit(amount)
            except Exception:
                print("Invalid amount,try again")
        elif action==3:
            account.Check_Balance()
        else:
            break
    else:
        print("Error : Invalid Option")