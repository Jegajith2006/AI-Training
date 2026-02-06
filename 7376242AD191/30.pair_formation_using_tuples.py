def pair_square(a):
    r = []
    for i in a:
        r.append((i, i*i))
    return r

a = list(map(int, input().split()))
print(pair_square(a))
