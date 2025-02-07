def si(p,r,t):
    i=(p*r*t)/100
    return i

print("Simple Interest")
p=float(input("Enter principal amount"))
r=float(input("Enter rate of interest"))
t=float(input("Enter time of interest"))

if(p>0 and r>0 and t>0):
    interest=si(p,r,t)
    print("Simple Interest is", interest)
else:
    print("Enter non-negative numbers")