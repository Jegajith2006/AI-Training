def pair(arr, k):
    c = 0
    n = len(arr)

    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] + arr[j] == k:
                c += 1

    print(c)

arr = list(map(int, input().split()))
k = int(input())
pair(arr, k)