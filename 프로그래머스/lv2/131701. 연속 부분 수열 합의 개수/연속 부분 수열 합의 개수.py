'''
문제 : 연속 부분 수열 합의 개수
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131701
'''
def solution(elements):
    answer = []
    n = len(elements)
    
    elements = elements + elements[:-1]
    
    # 처음 아이디어로 걍 해보자...
    
    for i in range(n):
        for j in range(n):
            answer.append(sum(elements[j:j+i+1]))
    answer = set(answer)
    
    return len(answer)

solution([7,9,1,1,4])