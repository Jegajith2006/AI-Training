def remove_ele(a, b):
    r = []
    for i in a:
        if i not in b:
            r.append(i)
    return r

a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(remove_ele(a, b))
