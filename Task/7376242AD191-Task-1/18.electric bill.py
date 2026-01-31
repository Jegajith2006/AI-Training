unit=int(input())
if unit<=100:
    s=0
elif unit<=300:
    s=(unit-100)*2
    if unit>200:
        s=s+50
else:
    s=(200*2)+((unit-300)*5)+100

print(s)
