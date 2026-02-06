def colsum(r,c):
    mat=[]
    for i in range(c):
        co=list(map(int,input().split()))
        mat.append(co)

    for i in range(c):
        s=0
        for j in range(r):
            s+=mat[j][i]
        print(s)
r=int(input())
c=int(input())
colsum(r,c)