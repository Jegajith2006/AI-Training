def co_word(s):
    w = s.split()
    r = {}
    for i in range(len(w)-1):
        p = (w[i], w[i+1])
        r[p] = r.get(p, 0) + 1
    return r

s = input()
print(co_word(s))
