import sys
from collections import deque

input = sys.stdin.readline

n, m, p = tuple(map(int, input().strip().split()))
grid = [input().strip() for _ in range(n)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dam_p = dict()
for _ in range(p):
    p, dam = input().strip().split()
    dam_p[p] = int(dam)
dis_p = []
HP = int(input().strip())


def find_boss():
    locs = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'B':
                locs.append((i, j, 0))
    return locs


def bfs(boss):
    # one turn(consuming length of q)
    # we starts searching from the loc of BOSS(B)
    # from B, it counts distance until we meet up players
    # we save each distance for each players
    # distance cnt: from smallest distance(as it takes seconds)
    # each second will give accumulated damage of arriving players
    # ex) (a, 2), (b, 3), (c, 3), (d, 5)
    # 3 4     5     6           total
    # A A+B+C A+B+C A+B+C+D     4A+3B+3C+D
    global dis_p
    bx, by, _ = boss[0]
    visit = [[0] * m for _ in range(n)]
    visit[bx][by] = 1
    q = deque(boss)
    while q:
        x0, y0, d = q.popleft()
        for i in range(4):
            nx, ny = x0 + dir[i][0], y0 + dir[i][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visit[nx][ny] or grid[nx][ny] == 'X':
                continue
            if grid[nx][ny] != '.':
                dis_p.append((grid[nx][ny], d + 1))
            q.append((nx, ny, d + 1))
            visit[nx][ny] = 1


def calc_incoming():
    global HP
    dis_p.sort(key=lambda x: x[1])
    cur, acc_dm, ans = 0, 0, 0
    while HP > 0:
        # distance 마다 봐도 되지만
        # 어떡할까, 짧은 거리부터 나오니까 도착했다고 가정하고
        # 다음 플레이어가 왔을때까지 데미지가 얼마나 들어갔는지 결정해야겠지?
        # 그러면 거리의 차이가 되겠다.
        for i in range(len(dis_p)):
            p, time = dis_p[i]  # take each player and arrving time
            HP -= (time - cur) * acc_dm  # if acc_dm counts, it gives attack of time()
            print(f'{p} is arrived by {time} from {cur}, HP damaged by accumulated hit by {acc_dm}, now HP is {HP}.')
            cur = time  # time update
            acc_dm += dam_p[p]
            if HP < 0:
                break
            ans += 1                 # 도착했으면 다음부터 때릴수 있다.
        break
    return ans


if __name__ == "__main__":
    locs = find_boss()
    bfs(locs)
    cnt = calc_incoming()
    print(cnt)
