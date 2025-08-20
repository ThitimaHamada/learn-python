#literal Pattern
service = 100
match service:
    case 1 : 
        print("預入")
    case 2 : 
        print("引き出し")
    case 3 : 
        print("残高")
    case _: #default case
        print("情報が間違っている")
