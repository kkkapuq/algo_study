n, c, g, h = map(int, input().split())

temperature = [list(map(int, input().split())) for _ in range(n)]

def doJob(a, b, n):
    if n < a:
        return c
    elif n >= a and n <= b:
        return g
    else:
        return h

answer = 0
for i in range(1, 1001):
    temp = 0
    for j in temperature:
        temp += doJob(j[0], j[1], i)
    
    answer = max(answer, temp)

print(answer)