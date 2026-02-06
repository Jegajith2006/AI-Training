def avg_stu(d):
    r = {}
    for k in d:
        r[k] = sum(d[k]) / len(d[k])
    return r

d = eval(input())
print(avg_stu(d))
