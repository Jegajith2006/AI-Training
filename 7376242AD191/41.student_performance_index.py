def perf_index(s):
    r = {}
    for i in s:
        r[i["name"]] = i["marks"]*0.7 + i["attendance"]*0.3
    t = max(r, key=r.get)
    return r, t

s = eval(input())
print(perf_index(s))
