
# def fact(number):
#     fact=1
#     for i in range(1,number+1):
#         fact=fact*i
#         i+=1
#     return fact

def fact(number):

    for i in range(number,0):
        number=number*i
        i=i-1
    return number

number=int(input("Enter non-negative integer"))

if (number>0):
    print(fact(number))
else:
    print("Invalid input,please enter non-negative integer")

