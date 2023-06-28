'''
문제 : n^2 배열 자르기
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/87390
'''
def solution(n, left, right):
    answer = []
    
    # 1. 10의 7승이면 10,000,000
    # 애초에 n*n 배열을 만들면 시초가 발생한다. 따라서 아이디어로 풀어야됨
    for i in range(left, right+1):
        num = 0
        if (i + 1) % n == 0:
            num = n
        else:
            d, m = divmod(i, n)
            # a번째 덩어리의 b번째 수
            a, b = d+1, m+1
            if b > a:
                num = a + (b-a)
            else:
                num = a
            
        answer.append(num)
    
    return answer