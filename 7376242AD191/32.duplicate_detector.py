def has_dup(a):
    return len(a) != len(set(a))

a = list(map(int, input().split()))
print(has_dup(a))
