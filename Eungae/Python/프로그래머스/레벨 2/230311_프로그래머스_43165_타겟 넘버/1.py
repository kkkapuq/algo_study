'''
문제 : 타겟 넘버
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/43165
'''
'''
1. 특정숫자 target을 만드는 방법의 수를 return
2. 백트래킹?
'''

import sys

sys.setrecursionlimit(10000)

answer = 0
numLen = 0
targets = 0
numbers = []

# def dfs(numLen, i, result, numbers, target):
#     if i == numLen:
#         if result == target:
#             global answer
#             answer += 1
#         return
#     dfs(numLen, i + 1, result + numbers[i], numbers, target)
#     dfs(numLen, i + 1, result - numbers[i], numbers, target)


def dfs(index, sum):
    # 탈출 조건
    if index == numLen:
        if sum == targets:
            global answer
            answer += 1
        return
    # 수행 동작
    dfs(index+1, sum+numList[index])
    dfs(index+1, sum-numList[index])
    
    
    

def solution(numbers, target):
    global answer, numLen, numList, targets
    
    numLen = len(numbers)
    targets = target
    numList = numbers
    
    dfs(0, 0)
    
    return answer

solution([1,1,1,1,1], 3)