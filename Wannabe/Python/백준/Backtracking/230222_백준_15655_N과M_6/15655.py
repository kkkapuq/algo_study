import sys
si = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

n, m = map(int,  si().strip().split())
nums = list(map(int, si().strip().split()))
nums.sort()

def helper(idx, used, pool):
    if used == m:
        print(*pool)
        return
    for k in range(idx+1, n):
        pool.append(nums[k])
        helper(k, used+1, pool)
        pool.pop()

for i in range(n-m+1):
    helper(i, 1, [nums[i]])
