import sys
si = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

n, m = map(int,  si().strip().split())
nums = list(map(int, si().strip().split()))
nums.sort()

def helper(used, pool):
    if used == m:
        print(*pool)
        return
    for k in range(n):
        if not visit[k]:
            pool.append(nums[k])
            visit[k] = 1
            helper(used+1, pool)
            visit[k] = 0
            pool.pop()

visit = [0]*n
for i in range(n):
    visit[i] = 1
    helper(1, [nums[i]])
    visit[i] = 0