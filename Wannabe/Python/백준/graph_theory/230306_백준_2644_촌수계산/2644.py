# design: make bond count btw two node
# nodes are 1~n indexed
# edges are given as parent-child relationship (there are m edges)
#  parent
# |     |
# ch    ch
# |    / |
# ch  ch ch
import sys

si = sys.stdin.readline
n = int(si().strip())
a, b = map(int, si().strip().split())
m = int(si().strip())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    p, ch = map(int, si().strip().split())
    g[p].append(ch)


def solution():
    p1, d1 = find_parent(a, 0)
    p2, d2 = find_parent(b, 0)
    if p1 == p2:
        print(d1 + d2)
        return
    else:
        print(-1)
        return


def find_parent(node, level):
    global g
    for i in range(1, n + 1):
        if node in g[i]:
            return find_parent(i, level + 1)
    return node, level


if __name__ == "__main__":
    solution()