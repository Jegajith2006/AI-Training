def tup_freq(t):
    r = {}
    for i in t:
        r[i] = r.get(i, 0) + 1
    return r

t = eval(input())
print(tup_freq(t))
