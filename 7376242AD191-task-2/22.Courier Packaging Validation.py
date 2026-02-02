l = int(input())
w = int(input())
h = int(input())

if l > 0 and w > 0 and h > 0:
    if l + w + h <= 150:
        print("ACCEPTED")
    else:
        print("REJECTED")
else:
    print("REJECTED")
