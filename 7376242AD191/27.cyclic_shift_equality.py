def cyclic(a, b):
    if len(a) != len(b):
        return False
    s = a + a
    return b in [s[i:i+len(b)] for i in range(len(a))]

a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(cyclic(a, b))
