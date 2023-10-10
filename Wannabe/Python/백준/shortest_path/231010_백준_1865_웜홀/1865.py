from collections import defaultdict
import sys


input = sys.stdin.readline
INF = int(1e9)
tc = int(input().strip())
for _ in range(tc):
    N, M, W = tuple(map(int, input().strip().split()))

    # 도로
    road = defaultdict(list)
    for _ in range(M):
        S, E, T = tuple(map(int, input().strip().split()))
        road[S].append((E, T))
        road[E].append((S, T))
    # 웜홀
    for _ in range(W):
        S, E, T = tuple(map(int, input().strip().split()))
        road[S].append((E, -T))

    distance = [INF] * (N + 1)

    distance[1] = 0                         # rnd
    for _ in range(N - 1):
        for s in road:
            for e, w in road[s]:
                distance[e] = min(distance[e], distance[s] + w)
    ans = False
    for s in road:
        for e, w in road[s]:
            if distance[e] > distance[s] + w:
                ans = True
                break
        if ans:
            break
    # yes or no
    if ans:
        print("YES")
    else:
        print("NO")