def dept_topper(s):
    r = {}
    for i in s:
        d = i["dept"]
        if d not in r or i["marks"] > r[d]["marks"]:
            r[d] = i
    return r

s = eval(input())
print(dept_topper(s))
