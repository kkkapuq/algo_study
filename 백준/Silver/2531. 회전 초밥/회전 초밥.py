'''
문제 : 회전 초밥
난이도 : 실버 1
소요 시간 : 
'''
import sys
from collections import deque
se = sys.stdin.readline

n, d, k, c = map(int, se().split())
sushi = [ int(se().rstrip()) for _ in range(n) ]
# 시간단축을 위한 덱 사용
# sushi = deque(sushi)

answer = 0

# 슬라이딩 윈도우 사용
for i in range(n):
    temp = set(sushi[:k])

    temp.add(c)
    answer = max(answer, len(temp))
    
    l = sushi.pop(0)
    sushi.append(l)

print(answer)
