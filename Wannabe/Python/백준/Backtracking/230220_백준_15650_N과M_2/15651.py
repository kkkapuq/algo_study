import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

n, m = map(int, input().strip().split())

def recur(idx, used, nums):
    if used == m:
        print(*nums)
        return
    for k in range(1, n+1):             # 중복허용하고 처음부터 시작가능
        nums.append(k)
        recur(k, used+1, nums)
        nums.pop()
        
for i in range(1, n+1):                 # 중복허용이기때문에 마지막 숫자부터 시작가능
    recur(i, 1, [i])