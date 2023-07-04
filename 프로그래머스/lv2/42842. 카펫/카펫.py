def solution(brown, yellow):
    answer = []
    size = brown + yellow
    # 전체 사각형의 x, y 값을 구할거임
    for x in range(1, size+1):
        # 넓이가 나누어 떨어지지 않으면 패스
        if size % x != 0:
            continue
        y = size / x
        print(x, y)
        # 세로가 더 큰 케이스는 제외
        if y > x:
            continue
        if yellow == size -(2*x) -(2*y) + 4:
            answer = [x, y]
            
    return answer