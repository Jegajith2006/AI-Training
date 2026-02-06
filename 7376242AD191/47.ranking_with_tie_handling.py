def rank_tie(a):
    r = {}
    s = sorted(set([i[1] for i in a]), reverse=True)
    for n, m in a:
        r[n] = s.index(m) + 1
    return r

a = eval(input())
print(rank_tie(a))
