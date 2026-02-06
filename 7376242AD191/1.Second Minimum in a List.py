def secmin(n):
    f = float('inf')
    s = float('inf')

    for i in n:
        if i < f:
            s = f
            f = i
        elif i < s and i != f:
            s = i

    print(s)

n = list(map(int, input().split()))
secmin(n)
