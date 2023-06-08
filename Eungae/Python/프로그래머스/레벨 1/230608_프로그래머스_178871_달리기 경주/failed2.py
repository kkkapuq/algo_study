from collections import OrderedDict

def solution(players, callings):
    answer = []
    # 1. 선수 : 등수 로 만들어진 map을 만든다.
    dic = OrderedDict()
    for i in range(len(players)):
        dic[players[i]] = i
        
    # 2. callings를 for문을 돌면서, 이전 map이랑 swap 해주자.
    for i in callings:
        if i in dic:
            # 2-1. 이름이 불려진 선수의 index를 dic에서 찾아와서, index-- 선수와 바꿔주는 작업
            l = list(dic.items())
            k = list(dic.keys())
            index = k.index(i)
            l[index - 1], l[index] = l[index], l[index - 1]
            dic = OrderedDict(l)
    
    for i in dic.keys():
        answer.append(i)

    # 3. 근데 이건 너무 파이써닉한 풀이인듯..?
    
    return answer

solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])