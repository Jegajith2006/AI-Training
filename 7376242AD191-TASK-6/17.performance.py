scores = list(map(float, input().split()))

avg = sum(scores)/len(scores)
variation = sum((x-avg)**2 for x in scores)/len(scores)

print("Average:", avg)
print("Variation:", variation)
