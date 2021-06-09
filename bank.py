from datetime import datetime

class Account():
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.balance=0
        self.transaction_fee=30
        self.loan=0
        self.loan_limit=5000
        self.interest=5
        self.transactions=[]
        self.withdrawals=[]
        self.borrow=[]


        

    def deposit(self,amount):
    
        if amount <=0:
            
            return "enter a valid amount"
        else:
            self.balance+=amount
            transaction={
                "amount":amount,
                "naration":"You deposited",
                "balance":self.balance,
                "time":datetime.now()
            }
            self.transactions.append(transaction)
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
            withdraw={
                "amount":amount,
                "naration":"You have withdrawn",
                "balance":self.balance,
                "time":datetime.now()
            }
            self.withdrawals.append(withdraw)
            return  (f" You have withdrawn {amount}, Your newbalance is {self.balance }")
def borrow(self,loan):
        loan_fees = self.loan_interest * loan / 100
        
        if loan < 0:
            return "Please enter a valid amount"

        elif loan > self.loan_limit:
            return "please enter a lower amount"

        elif  self.loan > 0:
            return "You have an outstanding loan"

        else:
            
            repay = loan + loan_fees
            self.loan += repay
            self.balance += loan
            borrowing={
                "amount":"amount",
                "naration":"You have borrowed",
                "balance":self.balance,
                "time":datetime.now()
                }
            self.borrow.append(borrowing)
            return f"You have received a loan of {loan} your account balance now is {self.balance},the amount you will repay is {self.loan}"
def repay(self,amount):
        if amount<=0:
            return "Pay more money"
        elif amount>self.loan:
            extra_amount=amount-self.loan
            self.balance+=extra_amount
            transaction={
                "amount":amount,
                "balance":self.balance,
                "narration":"You repaid",
                "time":datetime.now()
            }
            self.transactions.append(transaction)
            return "you have paid {} in excess. It has been added to your account".format(extra_amount)
        else:
            self.loan-=amount
            transaction={
                "amount":amount,
                "balance":self.balance,
                "narration":"You repaid",
                "time":datetime.now()
            }
            self.transactions.append(transaction)
            return "you have paid {}. outstanding loan balance is {}".format(amount,self.loan)

  
def get_statement(self): 
         for transaction in self.transactions :
            amount=transaction["amount"]
            naration=transaction["naration"]
            balance=transaction["balance"]
            time=transaction["time"]
            date=time.strftime("%D")
            print(f"{date}........ {naration}....... {amount}.......Balance {balance}")






        

