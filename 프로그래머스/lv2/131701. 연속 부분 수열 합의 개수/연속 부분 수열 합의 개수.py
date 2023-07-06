'''
문제 : 연속 부분 수열 합의 개수
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131701
'''
def solution(elements):
    answer = set()
    
    # 길이가 n일 때, 탐색해야 하는 인덱스는 [현재 인덱스 : 현재 인덱스 + 인덱스 % n] 이다.
    # 예를들어, 길이가 3인 연속 부분 수열에서 현재 인덱스가 4면, 4, 7, 9 임
    # if i == n-1: temp += elements[i-n]
    n = len(elements)
    
    for i in range(n):
        temp = 0
        for j in range(i, i+n):
            index = j
            temp += elements[j%n]
            answer.add(temp)

    return len(answer)