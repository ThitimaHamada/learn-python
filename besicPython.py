#local variable / global variable/variable scorp

balance = 1000 #global
def displayBalance():
    print("Account balance =",balance,"yen")

def deposit(value):
    global balance
    money =value #local 
    print("deposit =",money,"yen")
    if (money<=0):
        print("you can not do deposit")
        return
    
    balance+=money

def withdraw(value):
    global balance
    amount = value
    print("withdraw =",amount,"yen")
    if amount<=0 or amount>balance:
        print("you can not do withdraw")
        return
    
    balance-=amount

displayBalance()
withdraw(1200)
displayBalance()
