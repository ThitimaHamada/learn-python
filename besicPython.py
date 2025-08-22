#local variable / global variable/variable scorp

balance = 1000 #global
def displayBalance():
    print("Account balance =",balance,"yen")

def deposit(value):
    global balance
    money =value #local 
    print("deposit =",money,"yen")
    balance+=money

def withdraw(value):
    global balance
    amount = value
    print("withdraw =",amount,"yen")
    balance-=amount

displayBalance()
withdraw(500)
displayBalance()
