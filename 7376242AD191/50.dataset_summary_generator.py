def summary(d):
    r = {"rows": len(d), "unique_values": {}}
    for k in d[0]:
        r["unique_values"][k] = len(set(i[k] for i in d))
    return r

d = eval(input())
print(summary(d))
