'''
문제 : 사과 담기 게임
링크 : https://www.acmicpc.net/problem/2828
소요시간 : 
'''
import sys
se = sys.stdin.readline

n, m = map(int, input().split())
# 현재 바구니의 범위
s, e = 1, m
j = int(input())
dist = 0

for _ in range(j):
    apple = int(input())

    # 현재 바구니의 범위 내에 사과가 떨어지면 안움직임
    if apple >= s and apple <= e:
        continue
    else:
        # 현재 바구니 위치보다 왼쪽에 사과가 떨어지면 왼쪽으로 이동
        if apple < s:
            movement = s - apple
            s -= movement
            e -= movement
            dist += movement
        # 현재 바구니 위치보다 오른쪽에 사과가 떨어지면 오른쪽으로 이동
        elif apple > e:
            movement = apple - e
            s += movement
            e += movement
            dist += movement
print(dist)


