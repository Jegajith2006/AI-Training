n=int(input())
s=0
t=str(n)
while n>0:
    r=n%10
    s+=pow(r,len(t))
    n=n//10
if s==n:
    print("Armstrong")
else:
    print("Not")
    