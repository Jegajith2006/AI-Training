def top_k(a, k):
    r = {}
    for i in a:
        r[i] = r.get(i, 0) + 1
    s = sorted(r, key=r.get, reverse=True)
    return s[:k]

a = list(map(int, input().split()))
k = int(input())
print(top_k(a, k))
