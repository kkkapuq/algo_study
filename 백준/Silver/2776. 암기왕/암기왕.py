import sys

se = sys.stdin.readline

t = int(se())
for _ in range(t):
    n = int(se())
    set1 = set(map(int, se().split()))

    m = int(se())
    s = list(map(int, se().split()))

    for j in s:
        if j in set1:
            print(1)
        else:
            print(0)