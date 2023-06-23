n, k = map(int, input().split())
bombs = [ int(input()) for _ in range(n) ]

answer = 0

for i in range(n):
    for j in range(n):
        # 같은 위치일경우 체크x
        if i == j:
            continue

        # 폭발하는 범위 내라면 폭탄번호 갱신
        if abs(i - j) <= k and bombs[i] == bombs[j]:
            answer = max(answer, bombs[i])

print(answer if answer != 0 else -1)