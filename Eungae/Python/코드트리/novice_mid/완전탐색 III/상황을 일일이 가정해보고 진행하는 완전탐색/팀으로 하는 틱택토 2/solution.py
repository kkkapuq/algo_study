MAX_A = 3
MAX_X = 9

board = [
    list(map(int, input()))
    for _ in range(MAX_A)
]

ans = 0

# 모든 쌍에 대해 전부 시도해 봅니다.
for i in range(1, MAX_X + 1):
    for j in range(i + 1, MAX_X + 1):
        # i, j 두 명이 팀이 됐을 때 이길 수 있는지를 확인합니다.
        # win : 두 명이 팀이 됐을 때 이길 수 있다면 true
        win = False

        # num_i , num_j : 각 줄에 i, j가 나오는 개수
        num_i = 0
        num_j = 0

        # 가로로 빙고가 만들어질 때
        for k in range(MAX_A):
            num_i = 0
            num_j = 0
            for l in range(MAX_A):
                if board[k][l] == i:
                    num_i += 1
                if board[k][l] == j:
                    num_j += 1

            # 3개의 칸에 i, j가 총 3번 나오며
            # 둘 다 최소 1번 이상 나오면 승리
            if num_i + num_j == 3 and num_i >= 1 and num_j >= 1:
                win = True

        # 세로로 빙고가 만들어질 때
        for k in range(MAX_A):
            num_i = 0
            num_j = 0
            for l in range(MAX_A):
                if board[l][k] == i:
                    num_i += 1
                if board[l][k] == j:
                    num_j += 1

            # 3개의 칸에 i, j가 총 3번 나오며
            # 둘 다 최소 1번 이상 나오면 승리
            if num_i + num_j == 3 and num_i >= 1 and num_j >= 1:
                win = True

        # 왼쪽 위에서 오른쪽 아래를 잇는 대각선으로 빙고가 만들어질 때
        num_i = 0
        num_j = 0
        for k in range(MAX_A):
            if board[k][k] == i:
                num_i += 1
            if board[k][k] == j:
                num_j += 1

        # 3개의 칸에 i, j가 총 3번 나오며
        # 둘 다 최소 1번 이상 나오면 승리
        if num_i + num_j == 3 and num_i >= 1 and num_j >= 1:
            win = True


        # 오른쪽 위에서 왼쪽 아래를 잇는 대각선으로 빙고가 만들어질 때
        num_i = 0
        num_j = 0
        for k in range(MAX_A):
            if board[k][MAX_A - k - 1] == i:
                num_i += 1
            if board[k][MAX_A - k - 1] == j:
                num_j += 1

        # 3개의 칸에 i, j가 총 3번 나오며
        # 둘 다 최소 1번 이상 나오면 승리
        if num_i + num_j == 3 and num_i >= 1 and num_j >= 1:
            win = True


        if win:
            ans += 1

print(ans)