def norm(d):
    t=sum(d.values())
    for k in d:
        d[k]/=t
    print(d)

d=eval(input())
norm(d)
