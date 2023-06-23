import copy
n, b = map(int, input().split())
gifts = [ int(input()) for _ in range(n) ]
gifts.sort()
answer = 0

for i in range(n):
    cnt = 0
    temp = gifts[i] // 2
    gift = copy.deepcopy(gifts)
    if temp > b:
        answer = max(answer, cnt)
        continue
    else:
        cnt += 1
    del gift[i]
    for j in gift:
        temp += j
        if temp > b:
            answer = max(answer, cnt)
            continue
        else:
            cnt += 1
    answer = max(answer, cnt)

print(answer)