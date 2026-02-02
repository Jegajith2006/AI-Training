n = int(input())
t = n
rev = 0
while t > 0:
    rev = rev*10 + t%10
    t //= 10

for i in range(2, rev):
    if rev % i == 0:
        print("NOT PRIME")
        break
else:
    print("PRIME")
