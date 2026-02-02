n = int(input())
present = [0]*10
while n > 0:
    present[n%10] = 1
    n //= 10
for i in range(10):
    if present[i] == 0:
        print(i)
        break
