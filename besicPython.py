#Excetion
try:
    number1 = int(input("Enter number No.1:"))
    number2 = int(input("Enter number No.2:"))
    if number1<0 or number2<0:
        raise Exception("The numeric data must be positive only!")
    result = number1/number2
    print("Result = ",result)

except ValueError:
    print("The information incorrect,Please enter only number")
except ZeroDivisionError:
    print("Cannot be divided by zero")
finally:
    print("---------")
    print("End program")
    print("---------")