n = int(input())
t = n
rev = 0
while t > 0:
    rev = rev*10 + t%10
    t //= 10
print(n + rev)
