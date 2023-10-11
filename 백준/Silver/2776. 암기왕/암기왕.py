import sys

se = sys.stdin.readline

t = int(se().strip())
for i in range(t):
    set1 = set()
    n = int(se().strip())
    s = se().split()
    for j in s:
        set1.add(j)

    m = int(se().strip())
    s = se().split()

    for j in s:
        if j in set1:
            print(1)
        else:
            print(0)