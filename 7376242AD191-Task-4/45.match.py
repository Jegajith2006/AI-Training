def match(r,c):
    s=0
    for k in r:
        if k in c:
            s+=r[k]*c[k]
    print(s)

r=eval(input())
c=eval(input())
match(r,c)
