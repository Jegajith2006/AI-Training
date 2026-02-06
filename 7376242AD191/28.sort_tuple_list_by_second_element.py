def sort_tuple(t):
    r = sorted(t, key=lambda x: x[1], reverse=True)
    return r

t = eval(input())
print(sort_tuple(t))
