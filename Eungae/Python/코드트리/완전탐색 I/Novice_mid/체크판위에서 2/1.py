R, C = map(int, input().split())
square = []

for _ in range(R):
    square.append(list(map(str, input().split())))

answer = 0
for i in range(R):
    for j in range(C):
        for k in range(j+1, R-1):
            for l in range(j+1, C-1):
                if square[0][0] != square[i][j] and \
                   square[i][j] != square[k][l] and \
                   square[k][l] != square[R-1][C-1]:
                    answer += 1