def solution(strings, n):
    answer = []
    
    temp = []
    # [문자, 문자열, 인덱스] 로 구성된 2차원 배열을 만들고, 0번-1번 우선순위로 정렬 시킨다.
    for index, i in enumerate(strings):
        temp.append([i[n], i, index])
    temp.sort(key=lambda x:(x[0], x[1]))
        
    # 이렇게 생성된 2차원 배열을 for문 돌면서 answer에 넣어주기
    for i in temp:
        answer.append(i[1])
    
    return answer