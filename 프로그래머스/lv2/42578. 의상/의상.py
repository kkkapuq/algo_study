def solution(clothes):
    answer = 1
    
    dic = {}
    
    for cloth, cType in clothes:
        if cType not in dic:
            dic[cType] = [cloth]
        else:
            dic[cType].append(cloth)
    
    for i in dic.values():
        answer *= len(i) + 1
    
    return answer - 1