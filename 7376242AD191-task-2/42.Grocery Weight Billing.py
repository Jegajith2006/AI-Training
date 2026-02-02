w = float(input())
p = float(input())

amt = w * p

if w > 10:
    dis = amt * 5 / 100
    amt = amt - dis

print(amt)
