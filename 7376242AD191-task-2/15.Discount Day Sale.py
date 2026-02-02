a = int(input())
if a < 1000:
    pay = a
elif a < 3000:
    pay = a * 0.9
elif a < 5000:
    pay = a * 0.8
else:
    pay = a * 0.7
print(int(pay))
