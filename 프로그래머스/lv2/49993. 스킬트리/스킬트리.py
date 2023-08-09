'''
문제 : 스킬트리
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/49943
'''
from collections import deque
def solution(skill, skill_trees):
    answer = 0
    
    for i in skill_trees:
        q = deque(skill)
        # 스킬트리를 찍을 수 있는지 없는지 판단하는 플래그
        flag = True
        for j in i:
            # 1. i번째 단어가 skill 안에 있는 단어인지 확인한다.
            if j in skill:
                temp = q.popleft()
                # 2. 스킬트리 체크에 필요한 단어가 아니라면 패스하고, 체크가 필요하다면 검사를 진행한다.
                if j == temp:
                    continue
                else:
                    flag = False
        if flag:
            answer += 1
    
    return answer