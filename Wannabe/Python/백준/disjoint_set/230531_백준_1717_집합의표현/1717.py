# why union find ? since disjoint set comes to mind
# each operation has two options: join two or decide those are in same set
# initializing array for [0...n]
# before joining two, join when parent is different
# before checking two has same parent
import sys

sys.setrecursionlimit(int(1e3))

si = sys.stdin.readline

n, m = map(int, si().strip().split())
disjoint = [i for i in range(n + 1)]


def find_parent(node):
    if node == disjoint[node]:
        return node

    disjoint[node] = find_parent(disjoint[node])


def union(node_a, node_b):
    if node_a == node_b:
        return
    ap = find_parent(node_a)
    bp = find_parent(node_b)
    np = min(ap, bp)
    disjoint[ap] = np
    disjoint[bp] = np


def is_same(node_a, node_b):
    ap = find_parent(node_a)
    bp = find_parent(node_b)
    return ap == bp


if __name__ == "__main__":
    for _ in range(m):
        t, a, b = map(int, si().strip().split())
        if t == 0:
            union(a, b)
        else:
            if is_same(a, b):
                print("yes")
            else:
                print("no")