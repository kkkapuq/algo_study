'''
문제 : 택배상자
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131704
'''
from collections import deque

def solution(order):
    sub = deque()
    i = 1
    cnt = 0
    while i != len(order)+1:
        sub.append(i)
        while sub and sub[-1] == order[cnt]:
            cnt += 1
            sub.pop()
        i += 1

    return cnt
print(solution([4, 3, 1, 2, 5]))