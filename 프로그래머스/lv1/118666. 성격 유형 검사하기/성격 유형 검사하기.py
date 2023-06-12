def solution(survey, choices):
    answer = ''
    
    # 1. 유형별로 map을 선언해주고, 값이 높은 애를 성격 유형으로 정해준다.
    score = {"R" : 0,
             "T" : 0,
             "C" : 0,
             "F" : 0,
             "J" : 0,
             "M" : 0,
             "A" : 0,
             "N" : 0}
    
    # 2. survey for문을 돌면서, 점수를 매겨준다.
    for i in range(len(survey)):
        if choices[i] < 4:
            score[survey[i][0]] += abs(choices[i] - 4)
        elif choices[i] > 4:
            score[survey[i][1]] += choices[i] - 4
            
    # 3. 결과 도출
    if score["R"] == score["T"]:
        answer += 'R'
    else:
        answer += 'R' if score["R"] > score["T"] else 'T'
    
    if score["C"] == score["F"]:
        answer += 'C'
    else:
        answer += 'C' if score["C"] > score["F"] else 'F'
        
    if score["J"] == score["M"]:
        answer += 'J'
    else:
        answer += 'J' if score["J"] > score["M"] else 'M'
        
    if score["A"] == score["N"]:
        answer += 'A'
    else:
        answer += 'A' if score["A"] > score["N"] else 'N'
    
    return answer