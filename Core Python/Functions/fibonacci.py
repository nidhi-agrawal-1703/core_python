def fibonacci(l,n):
    for i in range(0, n):
        c = l[i + 1] + l[i]
        l.insert(i + 2, c)
        print(c)

n=int(input("Enter the number of terms in fibonacci series"))
l=[0,1]
print("Fibonacci Series")
for i in range(0, len(l)):
    print(l[i])
fibonacci(l,n)
