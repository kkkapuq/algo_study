import sys

n = int(input())

# 2차원 리스트 생성
Mat = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]

white,blue=0,0

def Color(x, y, n):
    global white, blue
    color = Mat[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if Mat[i][j] != color:
                Color(x, y+n//2, n//2)
                Color(x, y, n//2)
                
                Color(x+n//2, y, n//2)
                Color(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

Color(0, 0, n)
print(white)
print(blue)