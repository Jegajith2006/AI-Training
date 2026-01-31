ch=input("rec/cir:")
if ch=="rec":
    l=int(input())
    b=int(input())
    a=l*b
    p=2*(l+b)
    print("area=",a)
    print("permiter=",p)
else:
    r=int(input())
    a=3.14*(r**2)
    c=2*3.14*r
    print("area=",a)
    print("circum:",c)