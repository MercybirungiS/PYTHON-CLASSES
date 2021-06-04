class Account():
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.balance=0
        self.transaction_fee=30
        self.loan=0
        self.loan_limit=5000
        self.interest=0.5

    def deposit(self,amount):
        if amount <=0:
            return "enter a valid amount"
        else:
             self.balance+=amount
        return (f"Hello {self.name}.You have deposited {amount} . Your new balance is {self.balance}!")
    def withdraw (self,amount):
        total=amount+self.transaction_fee
        if amount <0:
            return ("Increase on the amount you want to withdraw")
            
        elif total>self.balance:

            return "You can not withdwaw any amount"
          
        else:
            self.balance-=total
            return  (f" You have withdrawn {amount}, Your newbalance is {self.balance }")
    def borrow  (self,loan):
        total =self.interest * loan
        total_amount=loan+total
        if loan>self.loan_limit:
            return "That is not a valid amount"
        elif loan > self.loan_limit:
            return "Your loan can not be greater than the loan limit"
        elif loan >0:
            return "You have an outstanding balance"
        else :
            self.loan=total_amount
            self.balance+=loan
            return (f"You have borrowed {loan} and you will be charged an interest of {total} .Your new account balance is {self.balance}")






        

        



    # def phone_Number(self):
    #     return f"Your account number is {self.acc_No}. Thank you for trusting us!"
    # def account_type(self):
    #return f"Your account type is {self.acc_type}.Thank you for trusting us !