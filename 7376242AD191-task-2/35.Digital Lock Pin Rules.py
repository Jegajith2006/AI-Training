n = int(input())
t = n
s = 0
c = 0

while t > 0:
    s = s + (t % 10)
    c = c + 1
    t //= 10

if c == 4 and s > 15:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
