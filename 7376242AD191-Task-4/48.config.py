def cfg(c,r):
    print(r-c.keys(), c.keys()-r)

c=eval(input())
r=set(input().split())
cfg(c,r)
