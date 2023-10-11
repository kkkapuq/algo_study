import heapq
import sys

se = sys.stdin.readline

n = int(se().strip())
hq = []

for i in range(n):
    temp = int(se().strip())
    if temp == 0:
        if not hq:
            print(0)
        else:
            print(heapq.heappop(hq)[1])
    else:
        heapq.heappush(hq, (abs(temp), temp))
