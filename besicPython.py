#OR pattern
data =input("Enter your prefix :")

match data:
    case "boy" | "mr.":
        print("male")
    case "girl" | "mrs." | "miss":
        print("female")
    case _:
        print("No information found")
