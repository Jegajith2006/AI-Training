numbers = list(map(float, input("Enter numbers: ").split()))

mean = sum(numbers) / len(numbers)
variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)

print("Spread (Variance):", variance)
