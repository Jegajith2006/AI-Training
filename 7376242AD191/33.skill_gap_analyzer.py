def skill_gap(r, s):
    m = r - s
    e = s - r
    return m, e

r = set(input().split())
s = set(input().split())
print(skill_gap(r, s))
