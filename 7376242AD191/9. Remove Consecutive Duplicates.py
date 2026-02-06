def remove_dup(a):
    r = [a[0]]
    for i in range(1, len(a)):
        if a[i] != a[i-1]:
            r.append(a[i])
    return r

a = list(map(int, input().split()))
print(remove_dup(a))
