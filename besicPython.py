#arge / kwargs

def saveEmployee(**kwargs): #tuple
    print(f"Name {kwargs["name"]},Department {kwargs["department"]}")
    print(f"Salary {kwargs["salary"]} yen")
    print(f"Address {kwargs["address"]} ")
    print("----------")


saveEmployee(name="Tawan",department="IT",salary=700000,address="Ueno")
saveEmployee(name="Nut",department="graphic",salary=800000,address="Tokyo")
saveEmployee(name="Jo",department="sale",salary=600000,address="Kyoto")



