def invert(d):
    r = {}
    for k, v in d.items():
        r.setdefault(v, []).append(k)
    return r

d = eval(input())
print(invert(d))
