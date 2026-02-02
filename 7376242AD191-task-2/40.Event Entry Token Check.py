n = int(input())

if n % 4 == 0:
    if n % 100 != 0:
        print("ENTRY")
    else:
        print("NO ENTRY")
else:
    print("NO ENTRY")
