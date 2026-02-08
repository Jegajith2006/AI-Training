def rank(a):
    s=sorted(set(i[1] for i in a),reverse=True)
    for n,m in a:
        print(n, s.index(m)+1)

a=eval(input())
rank(a)
