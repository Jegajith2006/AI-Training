def match_score(r, c):
    s = 0
    for k in r:
        if k in c:
            s += r[k] * c[k]
    return s

r = eval(input())
c = eval(input())
print(match_score(r, c))
