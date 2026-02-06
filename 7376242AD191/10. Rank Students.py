def stu(n, m):
    r = sorted(set(m), reverse=True)
    for i in range(len(n)):
        print(n[i], r.index(m[i]) + 1)

n = input().split()
m = list(map(int, input().split()))
stu(n, m)
