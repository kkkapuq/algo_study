import copy

n = int(input())
lines = [ tuple(map(int, input().split())) for _ in range(n)]

answer = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            # 같은 선분은 체크 x
            if i==j or i==k or j==k:
                continue
            
            arr = [0] * 100
            flag = True
            
            for l in range(n):
                if l == i or l == j or l == k:
                    continue
                for m in range(lines[l][0], lines[l][1]+1):
                    arr[m] += 1
                    if arr[m] > 1:
                        flag = False

            if flag:
                answer += 1

print(answer) 