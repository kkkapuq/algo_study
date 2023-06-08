def solution(players, callings):
    # 1. callings 만큼 for문을 돌고, 호출하는 선수가 players 에서 나타났을 때, 이전 선수와 swap 해주고 for문을 break 하고 다시 for문을 돌아준다.
    for i in range(len(callings)):
        for j in range(len(players)):
            # 1-1. players를 돌다가 호출한 선수가 있다면, i-- 번째 선수와 자리를 바꿔주고 break 해준다.
            if players[j] == callings[i]:
                temp = players[j-1]
                players[j-1] = callings[i]
                players[j] = temp
                break
    return players

solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])