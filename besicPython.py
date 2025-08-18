#九九
start = int(input("最初の九九:"))
end = int(input("最後の九九:"))

for number in range(start,end+1):
    print("九九",number)
    print("----------")
    for i in range(1,13):
        print(number,"x",i,"=",number*i)
    print("--------")
