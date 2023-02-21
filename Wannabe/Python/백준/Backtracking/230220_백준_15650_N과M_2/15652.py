import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

n, m = map(int, input().strip().split())

def recur(k, used, nums):
    if used == m:
        print(*nums)
        return
    
    for i in range(k, n+1):                     # 비내림차순이기에 k와 같은 수부터 붙여줌
        nums.append(i)
        recur(i, used+1, nums)
        nums.pop()
        
for i in range(1, n+1):                         # 중복허용이므로 n부터 시작가능
    recur(i, 1, [i])