import sys

input = sys.stdin.readline

matrix = [list(map(int, input().strip().split())) for _ in range(3)]

# zero counting
cnt = 0
for i in range(3):
    for j in range(3):
        if matrix[i][j] == 0:
            cnt += 1

# transpose
matrix_t = [[0] * 3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        matrix_t[i][j] = matrix[j][i]


# filled
def is_non_zero(mat):
    ret = []
    for i in range(3):
        ret.append(all(mat[i]))
    return all(ret)


if cnt == 3 and ((matrix[0][0] == 0 and matrix[1][1] == 0 and matrix[2][2] == 0) or
                 (matrix[0][2] == 0 and matrix[1][1] == 0 and matrix[2][0] == 0)):
    part_total = 0
    for i in range(3):
        part_total += sum(matrix[i])
    total = part_total // 2
    rem = []
    for i in range(3):
        rem.append(total - sum(matrix[i]))
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 0:
                matrix[i][j] = rem[i]

    for i in range(3):
        print(*matrix[i])
    exit(0)
else:
    total = 0
    part, part_t = [], []
    for i in range(3):
        if all(matrix[i]):
            total = sum(matrix[i])
        if all(matrix_t[i]):
            total = sum(matrix_t[i])
        part.append(matrix[i][i])
        part_t.append(matrix[i][2-i])
    if all(part):
        total = sum(part)
    if all(part_t):
        total = sum(part_t)
    while not is_non_zero(matrix):
        # scan through row or col that zero appears once
        part, part_t = [], []
        for i in range(3):
            cnt, cnt_r = 0, 0
            for j in range(3):
                if matrix[i][j] == 0:
                    cnt += 1
                if matrix_t[i][j] == 0:
                    cnt_r += 1
            if cnt == 1:
                part.append((i, total - sum(matrix[i])))
            if cnt_r == 1:
                part_t.append((i, total - sum(matrix_t[i])))

        for idx, v in part:
            for i in range(3):
                if matrix[idx][i] == 0:
                    matrix[idx][i] = v
        for idx, v in part_t:
            for i in range(3):
                if matrix_t[idx][i] == 0:
                    matrix_t[idx][i] = v

        for i in range(3):
            for j in range(3):
                if matrix[i][j] != matrix_t[j][i]:
                    matrix[i][j] = max(matrix[i][j], matrix_t[j][i])
                    matrix_t[j][i] = max(matrix[i][j], matrix_t[j][i])
    for i in range(3):
        print(*matrix[i])
    exit(0)
