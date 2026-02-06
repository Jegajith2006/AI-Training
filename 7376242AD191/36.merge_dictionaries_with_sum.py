def merge_sum(a, b):
    r = {}
    for k in a:
        r[k] = a[k] + b[k]
    return r

a = eval(input())
b = eval(input())
print(merge_sum(a, b))

