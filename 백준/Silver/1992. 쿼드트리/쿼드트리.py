import sys
se = sys.stdin.readline

# 데이터 입력 시작
n = int(se().rstrip())
arr = [ se().rstrip() for _ in range(n) ]
# 데이터 입력 끝

def recursion(r, c, size):
    color = arr[r][c]
    mid = size // 2
    for i in range(r, r+size):
        for j in range(c, c+size):
            if arr[i][j] != color:
                # 다르면 괄호 생성
                print('(', end='')
                recursion(r, c, mid)
                recursion(r, c+mid, mid)
                recursion(r+mid, c, mid)
                recursion(r+mid, c+mid, mid)
                print(')', end='')
                return
    print(color, end='')

recursion(0, 0, n)