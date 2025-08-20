#Capture Pattern
service = 2
match service:
    case 1 :
        print("預入")
    case 2 :
        print("引き出し")
    case 3 :
        print("残高")
    case service :
        print(f"Not found {service} in system please try again")
