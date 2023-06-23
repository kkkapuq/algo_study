# 사람, 치즈의 수, 치즈를 먹은 기록의 수, 아픈 기록 수
n, m, d, s = map(int, input().split())

# 몇번째 사람이, 몇번째 치즈를, 언제 먹었는지
eat = [ tuple(map(int, input().split())) for _ in range(d) ]
# eat.sort(key=lambda x:x[1])

# 몇번째 사람이, 언제 확실히 아팠는지
sick = [ tuple(map(int, input().split())) for _ in range(s) ]

# 시간대별로 상한 치즈를 놓아준다.
timeline = [[] for _ in range(101)]

# 1. n번째 사람이 t초에 아팠다면, 치즈를 먹은 시간 < t-1 이 된다.
# 2. 이 시간의 범위에 해당 치즈를 먹은 모든 사람은 배가 아플 예정이므로, 그 수만큼 약을 더해줘야 한다.

answer = 0
# 상한, 혹은 상했을 수도 있는 치즈 형식의 dic을 만들어준다.
# n번 치즈 : 아픈, 아플수도 있는사람들 형식
outDatedCheese = {}

# 아픈 사람을 기준으로 for문을 돌아보자.
# 한 번 돌아서 의심되는 치즈를 걸러주고, 그 치즈를 먹은 사람이 누가 있는지 다시 한번 탐색해주는 방식이다.
for i in sick:
    sickTime = i[1]
    sickPerson = i[0]
    for j in eat:
        eatPerson = j[0]
        eatCheese = j[1]
        eatTime = j[2]
        # 만약 아픈사람이 아픈시간이전에 치즈를 먹었으면, 해당 치즈는 상했을수있음
        if eatTime < sickTime and sickPerson == eatPerson:
            if eatCheese not in outDatedCheese:
                outDatedCheese[eatCheese] = [eatPerson]
            else:
                outDatedCheese[eatCheese].append(eatPerson)
        # 만약 내가 먹은 치즈에 다른 사람이 있으면 나도 아플 수도 있음
        else:
            if eatCheese in outDatedCheese:
                outDatedCheese[eatCheese].append(eatPerson)

# 한 번 돌았으니, 의심되는 치즈를 먹은 사람들을 더해주자
for i in eat:
    eatPerson = i[0]
    eatCheese = i[1]
    eatTime = i[2]
    # 만약 내가 먹은 치즈가 상한 치즈 리스트 안에 있으면 나도 아플 수도 있음
    if eatCheese in outDatedCheese:
        outDatedCheese[eatCheese].append(eatPerson)


# 이렇게 하면, 치즈별로 아픈사람들이 정리됨
for i in outDatedCheese.values():
    i = set(i)
    answer = max(answer, len(i))

print(answer)