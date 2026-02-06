def rev_dict(d):
    r = {}
    for k, v in d.items():
        r[v] = k
    return r

d = eval(input())
print(rev_dict(d))
