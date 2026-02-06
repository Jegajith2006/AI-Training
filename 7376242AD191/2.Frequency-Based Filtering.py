n = list(map(int, input().split()))
res = []

for i in n:
    if n.count(i) == 1:
        res.append(i)

print(res)