n = 4
arr = [1, 5, 2, 6]

max_sum = 0
for i in range(n):
    for j in range(i + 1, n):
        arr[i], arr[j] = arr[i] * 2, arr[j] * 2

        sum_diff = 0
        for k in range(n - 1):
            sum_diff += abs(arr[k + 1] - arr[k])

        max_sum = max(max_sum, sum_diff)
        arr[i], arr[j] = arr[i] // 2, arr[j] // 2

print(max_sum)