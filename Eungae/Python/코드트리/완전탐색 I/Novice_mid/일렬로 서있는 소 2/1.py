N = int(input())
cows = list(map(int, input().split()))
answer = 0

for i in range(N):
    for j in range(i+1, N):
        if cows[j] >= cows[i]:
            for k in range(j+1, N):
                if cows[k] >= cows[j]:
                    answer += 1

print(answer)