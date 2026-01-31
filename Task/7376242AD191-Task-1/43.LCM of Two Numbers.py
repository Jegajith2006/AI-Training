a = int(input())
b = int(input())


if a>b:
    m=a
else:
    m=b

while True:
    if m%a==0 and m%b==0:
        print("lcm=",m)
        break
    m+=1