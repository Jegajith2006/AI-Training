a=int(input())
b=int(input())
c=int(input())
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("Equilateral Triangle") 
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("not traingle")