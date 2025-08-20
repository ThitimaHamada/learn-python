#Mapping Pattern
customers = [
    {"name":"Tawan","type":"general"},
    {"name":"Jan","type":"member"},
    {"name":"Nan","type":"general"}

]
id = int(input("Enter your id:"))
print(f"Hello,your id is {id} : {customers[id]["name"]}")

match customers[id]:
    case {"type":"member"}:
        print("You are member 50% ")
    case _:
        print("No discount")



