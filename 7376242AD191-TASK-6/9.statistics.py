data = list(map(float, input().split()))

avg = sum(data)/len(data)
spread = sum((x-avg)**2 for x in data)/len(data)

print("Average:", avg)
print("Spread:", spread)
