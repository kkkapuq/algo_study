def solution(targets):
    answer = 0
    
    targets.sort(key=lambda x:x[1])
    cur = -1
    
    
    for s, e in targets:
        if s >= cur:
            answer += 1
            cur = e
    
    return answer