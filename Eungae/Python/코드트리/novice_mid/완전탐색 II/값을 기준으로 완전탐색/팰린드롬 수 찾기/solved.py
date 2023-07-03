x, y = map(int, input().split())
answer = 0

for i in range(x, y+1):
    temp = list(str(i))[::-1]
    if list(str(x)) == temp:
        answer += 1
print(answer)