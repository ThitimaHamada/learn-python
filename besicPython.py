#arge / kwargs

def saveEmployee(*args): #tuple
    print(f"Name {args[0]},Department {args[1]}")
    print(f"Salary {args[2]} yen")
    print(f"Address {args[3]} ")
    print("----------")


saveEmployee("Tawan","IT",700000,"Ueno")
saveEmployee("Nut","graphic",800000,"Tokyo")
saveEmployee("Jo","sale",600000,"Kyoto")



