def vocab_check(v, d):
    w = set()
    for i in d:
        w.update(i.lower().split())
    m = v - w
    p = (len(v)-len(m)) / len(v) * 100
    return p, m

v = set(input().split())
d = eval(input())
print(vocab_check(v, d))
