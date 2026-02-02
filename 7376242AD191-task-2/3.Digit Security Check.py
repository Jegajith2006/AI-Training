n=int(input())
a=[]
s=0
while n>0:
    r=n%10
    a.append(r)
    n//=10

for i in a:
    s+=i

if s%3==0 and a[0]%2==0:
    print("Valid")
else:
    print("not")