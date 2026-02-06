def normalize(d):
    t = sum(d.values())
    r = {}
    for k in d:
        r[k] = d[k] / t
    return r

d = eval(input())
print(normalize(d))
