#Guard Filter
# 100 = Get full score, 50-99 = Passed the test
score = int(input("Enter your score (0-100):"))
print("Your score is ",score)

match score:
    case 100 :
        print("Got a full score")
    case score if score >=50 and score < 100:
        print("Passed the exam")
    case _:
        print("Failed the exam")
