def vocab(s):
    r = set()
    for i in s:
        r.update(i.lower().split())
    return r

s = eval(input())
print(vocab(s))
