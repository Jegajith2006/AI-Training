n=int(input())
a=[]
while n>0:
    r=n%10
    a.append(r)
    n=n//10
print("".join(map(str, a)))

# or

n=int(input())
print((str(n))[::-1])