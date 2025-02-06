a=int( input("Enter first number"))
# b=int(input("Enter second number"))

# def sum(x,y):
#     c=x+y
#     return c
# print("Sum of ",a,"and ",b,"is",sum(a,b))

# def div(x,y):
#     if(y>0):
#         c=x/y
#         print(x,"/",y,"=",c)
# div(a,b)

def table(a):
    for i in range(1,11):
        c=a*i
        print(a,"*",i,"=",c)

table(a)
