n=int(input())
s=0
e=0
o=0
while n>0:
    r=n%10
    if r%2==0:
        e+=1
    else:
        o+=1
    n=n//10
print("Even=",e)
print("Odd=",o)