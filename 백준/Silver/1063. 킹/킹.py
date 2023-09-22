'''
문제 : 킹
링크 : https://www.acmicpc.net/problem/1069
소요시간 : 
'''
# 체스판 생성
grid = [ [0 for j in range(8)] for _ in range(8)]

# 북, 북동, 동, 남동, 남, 남서, 서, 북서 순
dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

# 명령에 따른 이동을 수행할 명령:인덱스 로 구성된 맵
move = {
    'R' : 2,
    'L' : 6,
    'B' : 4,
    'T' : 0,
    'RT' : 1,
    'LT' : 7,
    'RB' : 3,
    'LB' : 5
}

# 변수 초기화 
init = input().split()

# 킹과 돌의 좌표
# 행 - 숫자가 낮을수록 밑에서부터 올라오니까 8에서 빼준다. 
# 열 - 아스키 코드로 int화 해서 인덱스에 넣어주자.
kingR, kingC = 8 - int(init[0][1]), ord(init[0][0]) - ord('A')
stoneR, stoneC = 8 - int(init[1][1]), ord(init[1][0]) - ord('A')
n = int(init[2])

# 체스판 범위 체크
def in_range(x, y):
    return x >= 0 and x < 8 and y >= 0 and y < 8

# 이동 수행
for _ in range(n):
    order = input()
    dir = move[order]
    # 킹과 돌의 다음좌표
    kingNR, kingNC = kingR + dx[dir], kingC + dy[dir]
    stoneNR, stoneNC = stoneR + dx[dir], stoneC + dy[dir]

    # 현재 가려고 하는 자리에 돌이 있다면 밀어준다. 이 때, 범위를 벗어난다면 해당 명령은 수행하지 않는다.
    if kingNR == stoneR and kingNC == stoneC:
        if in_range(kingNR, kingNC) and in_range(stoneNR, stoneNC):
            kingR, kingC, stoneR, stoneC = kingNR, kingNC, stoneNR, stoneNC
        else:
            continue
    else:
        # 가려고 하는 자리에 돌이 없고, 킹이 이동했을 때 범위 안이라면 이동을 수행한다.
        if in_range(kingNR, kingNC):
            kingR, kingC = kingNR, kingNC

# 이동이 끝난 후 킹과 돌의 위치 구하기
# 행, 판에 맞게 8에서 빼주기
kingR = str(8 - kingR)
stoneR = str(8 - stoneR)

# 열, 아스키코드로 다시 문자열로 변환
kingC = chr(kingC + ord('A'))
stoneC = chr(stoneC + ord('A'))

print(kingC + kingR)
print(stoneC + stoneR)