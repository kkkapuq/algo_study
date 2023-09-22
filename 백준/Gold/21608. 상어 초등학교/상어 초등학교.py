'''
문제 : 상어 초등학교
링크 : https://www.acmicpc.net/problem/21608
소요시간 : 50분
'''
# 2. 1이 동일하면 남은 자리 많은대로
# 2-1. 동서남북을 둘러보고, 그 자리에서 또 동서남북 둘러봐서 빈 자리가 몇개인지 구한다. 이 값을 가지고 비교한다.
# 3. 2도 동일하면 행이 낮은대로, 이것도 동일하면 열이 낮은대로
# 3-1. 내가 갈 수 있는 곳이 리스트로 모여지면, 행-열 우선순위로 정렬시킨다.
# 4. 아무도 특정학생을 안좋아하는 경우도 있다.

# 인접하다는 것은 그냥 사방을 살펴보면 된다는 뜻. dx, dy를 사용하자.
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

# 순서대로 자리를 배정해준다. 따라서, 첫 번째 학생의 자리는 무조건 1,1 고정이다.

n = int(input())

grid = [ [0 for _ in range(n)] for _ in range(n)]
childmap = {}
students = []

# 좋아하는 친구들을 map에 할당해주는 작업
for _ in range(n*n):
    inputs = input().split()
    student = inputs[0]
    students.append(student)
    like = inputs[1:]

    childmap[student] = like

# 한명씩 자리 할당해주기, 첫 애는 자리 고정임
grid[1][1] = students[0]
for stu in students[1:]:
    # 1. 이 학생이 앉을 수 있는 비어있는 자리를 기준으로 한다. 좋아하는 애, 비어있는 칸, 행, 열 형태로 able에 넣어준다.
    able = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                # 해당 칸의 인접에 좋아하는 애 수, 비어있는 자리 수
                like, blank = 0, 0
                # 사방을 살펴본다.
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    # 범위 안인 경우만 탐색
                    if nx >= 0 and nx < n and ny >= 0 and ny < n:
                        # 만약 이 자리에 앉은애가 내가 좋아하는 애라면, like += 1
                        if grid[nx][ny] in childmap[stu]:
                            like += 1
                        elif grid[nx][ny] == 0:
                            blank += 1
                # i, j번 자리에 관련된 정보를 담아준다.
                able.append([like, blank, i, j])
    # 좋아하는 애와 빈 자리 수는 많을수록 앞에 와야하고, 행과 열은 작을수록 앞에 와야하니, 정렬조건을 이렇게 하자
    able.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
    # 정렬 후, 맨 앞에 있는 인덱스의 자리에 학생을 앉힌다.
    grid[able[0][2]][able[0][3]] = stu

answer = 0
for i in range(n):
    for j in range(n):
        temp = 0
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                # 주변에 좋아하는 학생이 있다면 temp += 1 해준다. 
                if grid[nx][ny] in childmap[grid[i][j]]:
                    temp += 1
        if temp == 0:
            answer += 0
        elif temp == 1:
            answer += 1
        elif temp == 2:
            answer += 10
        elif temp == 3:
            answer += 100
        elif temp == 4:
            answer += 1000

print(answer)