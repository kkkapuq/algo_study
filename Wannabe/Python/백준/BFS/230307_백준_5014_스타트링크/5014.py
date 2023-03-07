import sys
from collections import deque

si = sys.stdin.readline

# Today I learned: visit array makes time shorter / check node after pop the queue, it's different from checking candidate node / use cache
# design : get F, S, G, U, D
# F: # of entire floors
# S: current floor
# G: floor to go
# U: available upstair
# D: available downstair
# make bfs - available nxt node is cur+u or cur-d, and tuple has cnt as movement
# nxt node out of boundary should be skipped
# append nxt node to queue until it has no node found or found

F, S, G, U, D = map(int, si().strip().split())
visit = [0] * (F+1)


def bfs(node, start):
    visit[node] = 1
    q = deque([(node, start)])
    while q:
        nxt, cnt = q.popleft()
        if nxt == G:    return cnt
        for i in range(2):
            if i == 0:
                nxt_node = nxt + U
            else:
                nxt_node = nxt - D
            if nxt_node < 1 or nxt_node > F:    continue
            if not visit[nxt_node]:
                visit[nxt_node] = 1
                q.append((nxt_node, cnt + 1))
    return -1


ret = bfs(S, 0)
if ret == -1:
    print('use the stairs')
else:
    print(ret)
