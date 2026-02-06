def longest(a):
    m = c = 1
    for i in range(1, len(a)):
        if a[i] == a[i-1] + 1:
            c += 1
            m = max(m, c)
        else:
            c = 1
    return m

a = list(map(int, input().split()))
print(longest(a))

