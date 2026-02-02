h = int(input())
m = int(input())
x = int(input())

m = m + x
h = h + (m // 60)
m = m % 60
h = h % 24

print(h, m)
