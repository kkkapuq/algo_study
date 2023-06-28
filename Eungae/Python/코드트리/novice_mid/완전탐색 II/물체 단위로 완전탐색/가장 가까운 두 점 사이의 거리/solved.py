n = int(input())
dots = [ tuple(map(int, input().split())) for _ in range(n)]

distance = 99999999

for i in range(n):
    for j in range(i+1, n):
        temp = abs(dots[i][0] - dots[j][0]) * abs(dots[i][0] - dots[j][0]) + abs(dots[i][1] - dots[j][1]) * abs(dots[i][1] - dots[j][1])
        
        distance = min(distance, temp)

print(distance)