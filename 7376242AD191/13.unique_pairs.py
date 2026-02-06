def unique_pair(p):
    r = []
    for a, b in p:
        if (b, a) not in r:
            r.append((a, b))
    return r

p = eval(input())
print(unique_pair(p))
