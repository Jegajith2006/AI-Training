def swap(t):
    r = (t[1], t[0])
    return r

t = tuple(map(int, input().split()))
print(swap(t))
