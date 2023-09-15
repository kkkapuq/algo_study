def solution(routes):
    answer = 1
    # 요격 시스템이랑 비슷한 문제인거같은뎅
    # 나간지점 기준으로 내림차순 정렬해준다.
    routes.sort(key=lambda x:x[1])
    # [[-5, -3], [-14, -5], [-18, -13], [-20, -15]]
    # [[-20, -15], [-18, -13], [-14, -5], [-5, -3]]
    
    # 현재 카메라 위치 초기화
    cam = routes[0][1]
    # for문을 돌면서, 종료지점을 갱신해나간다.
    for s, e in routes:
        # 현재 카메라가 커버 가능한 범위면 지나감
        if s <= cam or e <= cam:
            continue
        else:
            # 만약, 현재 카메라 위치보다 종료지점이 더 앞서있다면, 카메라를 추가로 하나 배치해야 함
            answer += 1
            # 종료 위치 갱신
            cam = e
    
    return answer