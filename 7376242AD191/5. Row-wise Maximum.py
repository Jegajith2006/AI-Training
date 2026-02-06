def rowmax(r,c):
    mat=[]
    for i in range(r):
        ro=list(map(int,input().split()))
        mat.append(ro)

    for i in mat:
        print(max(i))
    # print(mat)
r=int(input())
c=int(input())
rowmax(r,c)