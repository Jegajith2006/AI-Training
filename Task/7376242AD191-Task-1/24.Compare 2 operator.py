a=int(input())
b=int(input())

s=a+b
t=a*b

if s>t:
    print(s,"is greater")
elif t>s:
    print(t,"is greater")
else:
    print("both are equal")