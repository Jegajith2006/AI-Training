n=int(input())
a=[]
while n>0:
    r=n%10
    a.append(r)
    n=n//10

e=o=0
for i in a:
    if i%2==0:
        e+=1
    else:
        o+=1
print(e,o)