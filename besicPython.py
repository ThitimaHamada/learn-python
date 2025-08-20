#Sequence pattern
data = [1,2]
match data:
    case []:
        print("No infornamation")
    case [1,2]:
        print("information are 1 and 2")
    case [1,2,3]:
        print("information are 1,2 and 3")
