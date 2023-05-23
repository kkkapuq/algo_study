N = int(input())
table = []
maxNum = 0

for _ in range(N):
    table.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N-2):
        maxNum = max(maxNum, table[i][j] + table[i][j+1] + table[i][j+2])
print(maxNum)