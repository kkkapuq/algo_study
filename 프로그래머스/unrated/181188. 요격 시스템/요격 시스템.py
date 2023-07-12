'''
문제 : 요격 시스템
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181188
'''

def solution(targets):
    answer = 1
    # 1. s, e 지점에서 발사한 요격미사일은 요격이 불가능한 점 숙지할 것
    # 2. 시작지점을 기준으로 정렬을 시켜보자.
    targets.sort(key=lambda x:x[0])
    
    # 요격 가능 범위 초기화
    S, E = -1, 100000001
    
    for i in range(len(targets)):
        s, e = targets[i][0], targets[i][1]
        
        # 3. 만약 기존에 수행하던 요격범위 내라면, 요격 기준위치를 갱신해준다.
        if s >= S and e <= E:
            S, E = s, e
        # 3-1. 기존 요격 범위(E) 안에서 시작하고, 끝나는 지점이 E보다 크다면 갱신 
        elif s < E and e > E:
            S, E = s, E
        else:
            # 3-2. 위 조건에 해당되지 않는 범위라면 새로 하나 쏴줘야됨, 현재 s, e값 갱신
            answer += 1
            S, E = s, e
        
    return answer
