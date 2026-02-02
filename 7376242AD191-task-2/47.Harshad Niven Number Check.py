n = int(input())
t = n
s = 0

while t > 0:
    s += t % 10
    t //= 10

if n % s == 0:
    print("Harshad Number")
else:
    print("Not Harshad Number")
