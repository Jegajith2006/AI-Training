def split(n):
    e=[]
    o=[]
    for i in n:
        if i%2==0:
            e.append(i)
        else:
            o.append(i)

    print("even list:",e)
    print("odd list:",o)
n=list(map(int,input().split()))
split(n)