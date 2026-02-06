def stats(a):
    r = (min(a), max(a), sum(a)/len(a))
    return r

a = list(map(int, input().split()))
print(stats(a))
