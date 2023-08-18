'''
문제 : 행렬 테두리 회전하기
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/77485
'''
import copy
def solution(rows, columns, queries):
    answer = []
    
    # grid 만들어주기
    grid = []
    for i in range(rows):
        temp = []
        for j in range(1, columns+1):
            temp.append(columns*i + j)
        grid.append(temp)
        
    # 탐색 시작
    for q in queries:
        r1, c1, r2, c2 = q[0]-1, q[1]-1, q[2]-1, q[3]-1
        
        # 회전할 때마다 비교해줘야됨
        smallest = grid[r1][c1]

        # 회전을 다 마친 후에, 좌상단 수를 한번 수기로 옮겨주는 작업을 진행해줘야 한다
        temp = grid[r1][c1]

        # 좌측 세로줄 (위쪽으로 미는 작업)
        for i in range(r1, r2):
            test = grid[i+1][c1]
            grid[i][c1] = test
            smallest = min(smallest, test)

        # 하단 가로줄 (왼쪽으로 미는 작업)
        for i in range(c1, c2):
            test = grid[r2][i+1]
            grid[r2][i] = test
            smallest = min(smallest, test)

        # 우측 세로줄 (아래쪽으로 미는 작업)
        for i in range(r2, r1, -1):
            test = grid[i-1][c2]
            grid[i][c2] = test
            smallest = min(smallest, test)

        # 상단 가로줄 (오른쪽으로 미는 작업)
        for i in range(c2, c1, -1):
            test = grid[r1][i-1]
            grid[r1][i] = test
            smallest = min(smallest, test)
        grid[r1][c1+1] = temp
        answer.append(smallest)
    return answer