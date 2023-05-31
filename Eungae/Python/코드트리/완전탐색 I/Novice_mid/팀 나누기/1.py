numbers = [1, 5, 3, 6]

def get_diff(i, j):
    sum1 = numbers[i] + numbers[i]
    sum2 = sum(numbers) - sum1
    return abs(sum1 - sum2)

min_diff = 100
for i in range(0, 4):
    for j in range(i+1, 4):
        min_diff = min(min_diff, get_diff(i, j))

print(min_diff)