def co(s):
    w=s.split()
    r={}
    for i in range(len(w)-1):
        p=(w[i],w[i+1])
        r[p]=r.get(p,0)+1
    print(r)

s=input()
co(s)
