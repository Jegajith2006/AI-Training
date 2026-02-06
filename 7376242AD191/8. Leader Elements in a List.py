def leader(n):
    m=0
    a=[]
    for i in n[::-1]:
        if(i>m):
            m=i
            a.append(i)
    print(" ".join(map(str, a[::-1])))

n=list(map(int,input().split()))
leader(n)   