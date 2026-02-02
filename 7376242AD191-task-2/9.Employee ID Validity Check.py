n=int(input())
a=[]
while n>0:
    r=n%10
    a.append(r)
    n//=10
if len(a)==6 and n%7==0:
    print("Valid")
else:
    print("Invalid")