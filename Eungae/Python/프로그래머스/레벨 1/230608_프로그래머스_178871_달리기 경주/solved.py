def solution(players, callings):
    answer = []
    # 1. 선수:등수 로 만들어진 map과 등수:선수 로 만들어진 map을 만든다.
    dic1, dic2 = {}, {}
    for i in range(len(players)):
        dic1[players[i]] = i
        dic2[i] = players[i]
    
    # 2. dic1에서 이 선수가 몇등인지 찾아내고, dic2에서 n등과 n-1등 선수를 바꿔준다.
    for i in callings:
        if i in dic1:
            grade = dic1[i]
            # 기존에 앞에 있던 선수, 추월할 선수
            prePlayer, nowPlayer = dic2[grade-1], dic2[grade]
            dic2[grade-1], dic2[grade] = dic2[grade], dic2[grade-1]
            dic1[prePlayer], dic1[nowPlayer] = dic1[nowPlayer], dic1[prePlayer]
    
    answer = list(dic2.values())

    return answer

solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])