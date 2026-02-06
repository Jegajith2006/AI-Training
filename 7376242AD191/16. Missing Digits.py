def miss(n):
    for i in range(10):
        if str(i) not in n:
            print(i,end=" ")
n=input()
miss(n)