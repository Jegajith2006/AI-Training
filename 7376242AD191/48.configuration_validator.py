def validate(c, r):
    m = r - c.keys()
    e = c.keys() - r
    return m, e

c = eval(input())
r = set(input().split())
print(validate(c, r))
