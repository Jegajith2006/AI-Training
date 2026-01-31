n=int(input())
a=[]
t=0
while n>0:
    r=n%10
    a.append(r)
    n//=10

for i in a:
    s=1
    for j in range(1,i+1):
        s*=j
    t+=s
if s==n:
    print("Strong number")
else:
    print("Not")