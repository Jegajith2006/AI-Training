n=int(input())
t=200
if n<5:
    s=t
    print("free--",s)
elif n>=5 and n<=12:
    s=t*0.5
    print("50%_discount--",s)
elif n>=13 and n<=59:
    s=t
    print("full ticket--",s)
else:
    s=t*0.3
    print("30%_discount--",s)
