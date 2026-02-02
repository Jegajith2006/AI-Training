n = int(input())
k = int(input())

s = n // k

if n % k != 0:
    s = s + 1

print(s)
