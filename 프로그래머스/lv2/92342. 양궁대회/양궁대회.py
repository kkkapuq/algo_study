'''
문제 : 양궁대회
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/92342
'''

from itertools import combinations_with_replacement as combi

def solution(n, info):
    answer = [-1]
    
    '''
    1. 같은 점수에 맞춘 갯수가 a(어피치), b(라이언) 이라면, a >= b 라면 어피치, 아니라면 라이언
    2. 총점이 a >= b 라면 어피치, 아니면 라이언
    3. 화살 개수 * 점수 가 아님, 몇개를 맞추던 그 점수 하나만 얻는거임
    4. 가장 큰 점수차로 우승할 수 있는 방법이 여러개면, 가장 낮은 점수를 더 많이 맞힌 경우를 return
    4-1. 그게 여러개면 그 다음 낮은수로 비교
    # info 길이가 11이니까 완탐 될거같음
    '''
    gap = 0
    
    # 0~10점까지 n개 중복조합으로 뽑고, 라이언 점수 할당해주기
    for combinated in combi(range(11), n):
        score = [0] * 11
        # 라이언 점수 할당해주기
        for i in combinated:
            score[10-i] += 1
            
        # 어피치, 라이언 점수
        a, l = 0, 0
        for index, i in enumerate(zip(info, score)):
            # 둘다 못맞췄으면 패스
            if i[0] == i[1] == 0:
                continue
            # 어피치가 이겼으면 어피치 점수 +
            elif i[0] >= i[1]:
                a += 10-index
            else:
                l += 10-index
                
        if l > a:
            # 점수차이가 기존에 비교한 조합보다 크다면 점수차이 갱신해주고, answer도 갱신해준다.     
            if abs(a-l) > gap:
                gap = abs(a-l)
                answer = list(score)
            # # 만약, 같은 점수차라면 더 낮은 점수를 많이맞춘 조합으로 갱신
            # elif abs(a-l) == gap:
            #     for i in range(10, -1, -1):
            #         if score[i] == info[i] == 0:
            #             continue
            #         if score[i] > info[i]:
            #             answer = list(score)
            #             break
    
    
    return answer

print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))