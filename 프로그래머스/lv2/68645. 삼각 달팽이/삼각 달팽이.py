'''
문제 : 삼각 달팽이
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/68645
'''
def solution(n):
    answer = [ [0] * i for i in range(1, n+1)]
    
    if n == 1:
        return [1]
    
    
    # 시뮬레이션에 사용될 dx, dy 비슷한 친구들
    # 순서대로 ↙, →, ↖ 방향
    dr, dc = [1, 0, -1], [0, 1, -1]
    
    # 들어갈 숫자, 방향변수, 최상단 초기화
    cnt = 2
    cDir = 0
    answer[0][0] = 1
    r, c = 0, 0
    
    # 범위 체크하는 함수, 행, 열, 행과 열의 길이가 파라미터로 들어감
    def outOfRange(tr, tc, lr, lc):
        return tr < 0 or tr >= lr or tc < 0 or tc >= lc 
    
    # ((n*(n+1))//2)+1
    # for문으로 돌면서 삽입
    for i in range(1, len(answer)):
        for j in range(len(answer[i])):
            # 다음 행과 열 체크
            nr, nc = r + dr[cDir], c + dc[cDir]
            # 전체 행의 길이(높이)와 현재 열의 길이(너비)
            lr, lc = len(answer), len(answer[r])
            
            # 범위 외이거나, 다음 좌표에 이미 다른 수가 채워진 경우, 방향을 전환한다.
            if outOfRange(nr, nc, lr, lc) or answer[nr][nc] != 0:
                cDir = (cDir + 1) % 3
            
            # 방향이 변경된거 반영해줘야됨
            r, c = r + dr[cDir], c + dc[cDir]
            answer[r][c] = cnt
            cnt += 1

    temp = []
    for i in answer:
        for j in i:
            temp.append(j)
    
    return temp
