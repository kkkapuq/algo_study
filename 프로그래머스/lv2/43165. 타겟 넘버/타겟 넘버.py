'''
문제 : 타겟 넘버
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/43165
'''
import sys

sys.setrecursionlimit(10000)

answer = 0

def dfs(target, numbers, idx, numberSum):
    # 만약 numbers의 끝까지 탐색을 완료했다면, 조건을 만족할 때 answer+=1 해준다.
    if idx == len(numbers):
        if numberSum == target:
            global answer
            answer += 1
        return

    # 빼기와 더하기를 직접 수행해준다.
    dfs(target, numbers, idx+1, numberSum + numbers[idx])
    dfs(target, numbers, idx+1, numberSum - numbers[idx])

def solution(numbers, target):
    global answer
    
    # 1. dfs로 하나씩 다 검사해본다.
    # 2. 요소는 각각 타겟넘버/숫자배열/인덱스/i까지 숫자들의 합 으로 이루어진다.
    dfs(target, numbers, 0, 0)
    
    return answer
