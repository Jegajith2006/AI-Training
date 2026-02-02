n=int(input())
a=[]
fs=ls=0
while n>0:
    r=n%10
    a.append(r)
    n//=10
b=int(len(a)/2)

for i in a[b:]:
    fs+=i
for i in a[:b]:
    ls+=i

if fs==ls:
    print("Balanced")
else:
    print("Not")