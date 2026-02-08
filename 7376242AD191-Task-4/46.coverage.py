def cov(v,d):
    w=set()
    for i in d:
        w|=set(i.split())
    print((len(v&w)/len(v))*100, v-w)

v=set(input().split())
d=eval(input())
cov(v,d)
