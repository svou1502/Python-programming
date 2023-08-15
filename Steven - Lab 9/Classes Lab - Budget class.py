class Budget:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        Total = Total - self.budget

    def withdraw (self, amount):
        self.balance = self.balance - amount
        return self.balance

    def deposit (self, amount):
        self.balance = self.balance + amount
        return self.balance

    def balance (self):
        return self.balance
        
    def transfer(self, amount, transfer):
        transfer += amount
        self.balance -=amount

clothing = Budget(100) # giving clothing a pre-budget of 100
entertainment = Budget() # no budget
food=Budget()

clothing.withdraw(20)
print ('Clothing budget is now',clothing.Budget)
       
# Requesting deposit and withdrawal inputs

#amount = float(input("Enter deposit amount: "))
#withdrawn_amount = float(input("Enter withdrawn amount: "))
#balance = print(f"Your balance is: " {self.balance()})

#clothing = Budget(0)
#entertainment = Budget(0)

#clothing.withdraw(20)
#entertainment.deposit(5)


