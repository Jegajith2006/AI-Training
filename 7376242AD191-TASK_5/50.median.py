numbers = list(map(float, input("Enter numbers: ").split()))
numbers.sort()

n = len(numbers)

if n % 2 == 1:
    print("Median:", numbers[n // 2])
else:
    mid = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    print("Median:", mid)
