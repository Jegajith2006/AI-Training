def common(a, b, c):
    r = list(set(a) & set(b) & set(c))
    return r

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
print(common(a, b, c))
