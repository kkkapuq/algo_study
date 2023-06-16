n = int(input())
strings = list(input())
cnt = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if strings[i] == 'C' and strings[j] == 'O' and strings[k] == 'W':
                cnt += 1

print(cnt)