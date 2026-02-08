def dr(a):
    s=[]
    for i in a:
        if i in s:
            print(i)
        s.append(i)

a=eval(input())
dr(a)
