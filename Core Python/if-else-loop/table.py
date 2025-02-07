number=float(input("Enter a non-negative number"))

if(number>0):
    for i in range(1,11):
        print(number,"x",i,"=",number*i)
else:
    print("Invalid input,please enter non-negative number")