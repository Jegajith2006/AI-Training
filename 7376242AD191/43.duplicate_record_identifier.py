def find_dup(a):
    r = []
    seen = []
    for i in a:
        if i in seen and i not in r:
            r.append(i)
        else:
            seen.append(i)
    return r

a = eval(input())
print(find_dup(a))
