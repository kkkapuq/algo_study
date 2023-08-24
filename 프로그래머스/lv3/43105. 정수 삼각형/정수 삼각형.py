'''
문제 : 정수 삼각형
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/43105
'''
def solution(triangle):
    n = len(triangle)
    
    for i in range(1, n):
        for j in range(len(triangle[i])):
            # 왼쪽 원소인 경우
            if j == 0:
                triangle[i][0] += triangle[i-1][0]
            # 오른쪽 원소인 경우
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]
            # 사이 원소인 경우
            else:
                triangle[i][j] = max(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]
    
    return max(triangle[n-1])