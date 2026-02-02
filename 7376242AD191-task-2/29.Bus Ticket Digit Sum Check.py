n = int(input())
s = 0

while n > 0:
    s = s + (n % 10)
    n //= 10

if s % 9 == 0:
    print("VALID")
else:
    print("INVALID")
