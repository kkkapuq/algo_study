from collections import deque
import sys

si = sys.stdin.readline


def bfs(node):
    global edges, visit
    in_edges = set()
    q = deque([node])
    while q:
        node1 = q.popleft()
        for nxt in edges[node1]:
            if nxt not in visit:
                visit.add(nxt)
                in_edges.add((node1, nxt))
                in_edges.add((nxt, node1))
                q.append(nxt)
                continue
            if (node1, nxt) not in in_edges:
                return False
    return True


case = 0
while True:
    case += 1
    visit = set()
    cnt = 0
    n, m = map(int, si().strip().split())
    if n == 0 and m == 0:
        exit()
    edges = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, si().strip().split())
        edges[a].append(b)
        edges[b].append(a)

    for i in range(1, n + 1):
        if i not in visit:
            visit.add(i)
            if bfs(i):
                cnt += 1

    print(f'Case {case}: ', end='')
    if cnt == 0:
        print('No trees.')
    elif cnt == 1:
        print('There is one tree.')
    else:
        print(f'A forest of {cnt} trees.')