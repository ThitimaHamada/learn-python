#Create Function
def sayHello(time,username,age): #parameter
    print("Hello",time,username)
    print("This year you are",age,"years old")

def saveEmployee(name,departmemt,salary):
    print(f"Name {name},Department {departmemt}")
    print(f"Salary {salary} yen")

def showTable(num):
    print("---------")
    for i in range(1,13):
        print(f"{num} x {i} = {num*i}")

#mytime = "morning"
#sayHello(mytime,"Tawan",31) #argument
#sayHello(mytime,"Jojo",25)
#showTable(3)
#showTable(5)
saveEmployee("Tawan","IT",700000)
saveEmployee("Nut","graphic",800000)
saveEmployee("Jo","sale",600000)



