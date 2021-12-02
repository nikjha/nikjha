#!/usr/bin/python3
class BankAccount :

    def set_details(self, name= None, balance=0):
        name=input("Enter your name ")
        balance = int(input("Enter your opening balance "))
        self.name =name
        self.balance = balance


    def display(self):
        print(self.name, self.balance)

    def withdraw(self):
        #amount = input("Enter the amount you want to withdraw ")
        amount = int(input("Enter the amount you want to withdraw "))

        '''if type(amount) is int:
            pass
        elif type(amount) is float:
           amount = int(amount)
           pass
        else:
            amount = int(input("Please enter only numbers :"))'''

        if(self.balance >= amount):
            self.balance -= amount
            print(self.name, " your remaining balance is ", self.balance)
        else:
            print("Insufficient Fund and can not be withdrawn")
            self.deposit()

    def deposit(self):
        amount = int(input('Please enter the  amount you want to deposit :'))
 #       self.balance = int(self.balance) + int(amount)
        self.balance += amount
        print(self.name, "Your remaing balance is ", self.balance)


ba = BankAccount()
ba.set_details()
ba.display()
ba.withdraw()
#ba.deposit()




