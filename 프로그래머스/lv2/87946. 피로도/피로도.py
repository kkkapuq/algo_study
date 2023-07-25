from itertools import permutations as pm

def solution(k, dungeons):
    answer = -1
    
    # 순열로 풀면 될듯?
    for i in list(pm(dungeons, len(dungeons))):
        # 현재 피로도와 클리어한 던전 수
        pirodo, clear = k, 0
        for j in i:
            # 입장 피로도와 소모 피로도
            toIn, toUse = j[0], j[1]
            if toIn <= pirodo:
                pirodo -= toUse
                clear += 1
            else:
                break
        answer = max(answer, clear)
    
    return answer