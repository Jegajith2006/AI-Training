a = int(input())
count = 0
for note in [500,200,100,50,20,10,1]:
    count += a // note
    a %= note
print(count)
