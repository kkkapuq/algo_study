def solution(dirs):
    answer = 0
    
    # 1. 명령어에 따른 x, y 좌표값의 변동을 dx, dy 처럼 맵으로 표현한다.
    move = {
        'U' : (0, 1),
        'D' : (0, -1),
        'R' : (1, 0),
        'L' : (-1, 0)
    }
    
    # 2. 시작좌표 -> 이동좌표 를 맵으로 만들어준다.
    went = {}
    
    # 좌표 초기화
    x, y = 0, 0
    for i in dirs:
        # 이동하는 좌표가 경계 밖이라면 무시
        nx, ny = x + move[i][0], y + move[i][1]
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        
        if str([x, y, nx, ny]) not in went or str([nx, ny, x, y]) not in went:
            answer += 1
            went[str([x, y, nx, ny])] = 1
            went[str([nx, ny, x, y])] = 1
        
        x, y = nx, ny
    
    return answer