a=float(input("Enter the first side "))
b=float(input("Enter the second side"))
c=float(input("Enter the third side"))
if a+b>c:
    s = (a + b + c) / 2
    d = (s*(s-a)*(s-b)*(s-c))**0.5
    print("Area of triangle is", d)
    
else:
    print("invalid sides")    