def group_words(w):
    r = {}
    for i in w:
        l = len(i)
        r.setdefault(l, []).append(i)
    return r

w = input().split()
print(group_words(w))
