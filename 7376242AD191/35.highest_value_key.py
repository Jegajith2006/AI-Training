def high_key(d):
    r = max(d, key=d.get)
    return r

d = eval(input())
print(high_key(d))

