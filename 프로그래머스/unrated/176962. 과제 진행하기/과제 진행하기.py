'''
문제 : 과제 진행하기
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/176962
'''
def timeToMinute(t):
    t = t.split(':')
    return int(t[0])*60 + int(t[1])

def solution(plans):
    answer = []
    # 0. 시간 계산은 모두 분으로 통일시켜서 진행한다.
    # 1. 도중에 멈춘 과제를 처리해줄 stack을 생성한다.
    stack = []
    # 2. plans 배열을 시작순으로 정렬해준 sortedPlans 에 넣어준다.(NlogN)
    sortedPlans = []
    for i in plans:
        name, start, playtime = i[0], timeToMinute(i[1]), int(i[2])
        sortedPlans.append([name, start, playtime])
    sortedPlans.sort(key=lambda x:x[1])
    # 현재 시간을 의미하는 t 를 첫 과제의 시작시간으로 초기화해준다.
      # 반례 : [["A", "11:50", "30"], ["B", "13:00", "20"], ["C", "13:10", "30"]]
      # 답 : ["A","C","B"], 출력 : ["A","B","C"]
      # 과제를 완료하고도 붕 떠있는 시간이 있어서, 현재시간으로 비교해가면서 하는 방법 자체가 잘못됐음. 
      # t = sortedPlans[0][1]

    # 3. for문을 돌면서, a과제를 하다가 b과제를 해야되면 stack에 넣어준다.
    for i in range(len(sortedPlans)):
        # 현재 과제
        Aname, Astart, Aplaytime = sortedPlans[i][0], sortedPlans[i][1], sortedPlans[i][2]
        # 마지막 과제는 stack에 넣어서 후처리 진행
        if i == len(sortedPlans) - 1:
            stack.append([Aname, Aplaytime])
            break
        # 다음 과제 시작시간
        Bstart = sortedPlans[i+1][1]
        # 다음 과제 전까지 수행이 가능하면 현재 과제 수행 이후 스택과제 수행
        if Astart + Aplaytime <= Bstart:
            answer.append(Aname)
            # 다음 과제 전까지 스택과제를 수행 가능한 시간
            t = Bstart - (Astart + Aplaytime)
            while t != 0 and stack:
                Sname, Splaytime = stack[-1][0], stack[-1][1]
                # 스택과제 수행이 가능하다면 정답배열에 넣어주기
                if Splaytime <= t:
                    answer.append(Sname)
                    stack.pop()
                    t -= Splaytime
                else:
                    # 아니라면, 진행도만 업데이트 해주기
                    stack[-1][1] = Splaytime - t
                    t = 0
                    break
        else:
            # 4-1. 못끝낸다면 현재시간 갱신해주고 stack에 넣기
            stack.append([Aname, Aplaytime - (Bstart - Astart)])
            
    # 5. stack에 남아있는 친구들 정리
    while stack:
        answer.append(stack[-1][0])
        stack.pop()
    
    return answer
