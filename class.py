from bank import MobileMoneyAccount
mm=MobileMoneyAccount("Mercy","099887","Airtel")
print(mm.deposit(1000))
print (mm.buy_airtime(50))
mm.statement()
