'''
문제 : 공원 산책
난이도 : 레벨 1
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/172928
'''

def isMove(park, position, op, cnt):
    # n X m 의 격자
    n, m = len(park[0]), len(park)
    temp = []
    
    # 1. 현재 위치에서 주어진 방향으로 이동할 때 공원을 벗어나는지?
    if op == 'N':
        if (position[0] - cnt < 0 or position[0] - cnt >= m):
            return False
        # 2. 주어진 방향으로 이동 도중, 장애물을 만나는지?
        for i in range(position[0]-1, position[0] - cnt - 1, -1):
            if park[i][position[1]] == 'X':
                return False
    elif op == 'S':
        if(position[0] + cnt < 0 or position[0] + cnt >= m):
            return False
        for i in range(position[0]+1, position[0] + cnt + 1):
            if park[i][position[1]] == 'X':
                return False
    elif op == 'E':
        if (position[1] + cnt < 0 or position[1] + cnt >= n):
            return False
        for i in range(position[1]+1, position[1] + cnt + 1):
            if park[position[0]][i] == 'X':
                return False
    elif op == 'W':
        if (position[1] - cnt < 0 or position[1] - cnt >= n):
            return False
        for i in range(position[1]-1, position[1] - cnt - 1, -1):
            if park[position[0]][i] == 'X':
                return False
    return True

def solution(park, routes):
    answer = []
    # n X m 의 격자
    n, m = len(park[0]), len(park)
    
    # 2. S를 찾을때까지 2중 for문 돌다가, 찾으면 좌표를 저장하기
    start = []
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                start = [i, j]
                break
        if len(start) > 0:
            break
    
    # 3. isMove가 True라면 위치 이동시켜주기
    for i in routes:
        # 이동좌표, 이동거리
        op, cnt = i.split()[0], int(i.split()[1])
        if isMove(park, start, op, cnt):
            if op == 'N':
                start = [start[0]-cnt, start[1]]
            if op == 'S':
                start = [start[0]+cnt, start[1]]
            if op == 'E':
                start = [start[0], start[1]+cnt]
            if op == 'W':
                start = [start[0], start[1]-cnt]
    # 4. 마지막 답 return
    return start

solution(["SOO","OOO","OOO"], 	["E 2","S 2","W 1"])