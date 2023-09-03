a=int(input("Enter the seconds"))
b=a//3600
c=a%3600//60
d=a%3600%60
print("hours", b)
print("minutes", c)
print("seconds", d)