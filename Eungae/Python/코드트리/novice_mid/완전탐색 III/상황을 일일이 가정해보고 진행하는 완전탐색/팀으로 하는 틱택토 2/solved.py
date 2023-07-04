arr = [list(input()) for _ in range(3)]
answer = 0

# 가로, 세로, 대각을 체크한다.
# for문을 돌면서, 해당 배열에 팀을 맺은 두 숫자로 빙고가 안되면 False를 return해준다.

def horizon(a, b):
    for i in range(3):
        flag = True
        team = set()
        for j in range(3):
            # 승리할 수 없다면 flag를 False로 바꿔준다.
            if not (arr[i][j] == a or arr[i][j] == b):
                flag = False
            if arr[i][j] == a or arr[i][j] == b:
                team.add(arr[i][j])
        # 한 줄이라도 승리할 수 있다면 True로 return해준다.
        if flag and len(team) == 2:
            return True
    return False

def vertical(a, b):
    for i in range(3):
        flag = True
        team = set()
        for j in range(3):
            if not (arr[j][i] == a or arr[j][i] == b):
                flag = False
            if arr[i][j] == a or arr[i][j] == b:
                team.add(arr[j][i])
        if flag and len(team) == 2:
            return True
    return False

def diagonal(a, b):
    flag = False
    team = set()

    if (arr[0][0] == a or arr[0][0] == b) and \
        (arr[1][1] == a or arr[1][1] == b) and \
        (arr[2][2] == a or arr[2][2] == b):
        flag = True
        team.add(arr[0][0])
        team.add(arr[1][1])
        team.add(arr[2][2])

    if (arr[0][2] == a or arr[0][2] == b) and \
        (arr[1][1] == a or arr[1][1] == b) and \
        (arr[2][0] == a or arr[2][0] == b):
        flag = True
        team.add(arr[0][2])
        team.add(arr[1][1])
        team.add(arr[2][0])

    if flag and len(team) == 2:
        return True
    return False

# 플레이어가 누군지 저장할 리스트
member = []

for i in arr:
    for j in i:
        if j not in member:
            member.append(j)

# 플레이어끼리 팀을 맺는 경우의 수
for i in range(len(member)):
    for j in range(i+1, len(member)):
        a, b = member[i], member[j]
        if horizon(a, b) or vertical(a, b) or diagonal(a, b):
            answer += 1

print(answer)