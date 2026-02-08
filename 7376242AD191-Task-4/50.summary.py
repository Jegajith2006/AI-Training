def summ(a):
    r={"rows":len(a),"unique_values":{}}
    for k in a[0]:
        r["unique_values"][k]=len(set(i[k] for i in a))
    print(r)

a=eval(input())
summ(a)

