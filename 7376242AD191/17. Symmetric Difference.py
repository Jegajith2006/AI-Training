def sym(a, b):
    r = list(set(a) ^ set(b))
    return r

a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(sym(a, b))
