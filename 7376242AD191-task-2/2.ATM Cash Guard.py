bal=int(input())
am=int(input())
if am%100==0:
    print("success")
elif am<=bal:
    print("success")
elif (bal-am)>=500:
    print("success")
else:
    print("reject")
