'''
문제 : 기사단원의 무기
난이도 : 레벨 1
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/136798?language=python3
'''
'''
1. 제한수치 초과한 사람은 power를 사용
2. 약수를 구해서, 그 약수가 limit 보다 크다면 power로 설정,
3. answer += 위 계산을 통해서 나온 철의 무게
'''
import math

def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number+1):
        temp = yaksu(i)
        print(temp)
        if temp > limit:
            answer += power
        else:
            answer += temp
    
    return answer

def yaksu(n):
    # 1은 모든 수의 약수
    cnt = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            cnt += 1
            if i ** 2 != n:
                cnt += 1
    
    return cnt

solution(18, 3, 2)