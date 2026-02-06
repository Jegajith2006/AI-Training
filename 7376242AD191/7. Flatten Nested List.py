def flattenlist(n):
    a=[]
    b=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
    for i in a:
        for j in i:
            b.append(j)
    print(b)

n=int(input())
flattenlist(n)