#para + return function
def checkNumber(number):
    if number%2==0:
        return "ku"
    else:
        return "ki"

def summation(*data):
    total = 0
    for item in data:
        total+=item
    return total


#result = checkNumber(13)
#print("Result =",result)
print(summation(10,20))
print(summation(10,20,30))




