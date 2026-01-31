a=int(input())
b=int(input())
c=int(input())

d=(b**2)-4*a*c
if d>0:
    print("Real & Distinct")
elif d==0:
    print("Real & Equal")
else:
    print("Imaginary")