'''
문제 : N과 M(3)
난이도 : 실버 3
링크 : https://www.acmicpc.net/problem/15651
'''
'''
1. s로 수열을 만드는데, 마지막 숫자까지는 중복이 허용 된다. 마지막은 한번만 허용.
2. 
'''

n, m = map(int, input().split())
# 4, 2로 예를들자
s = []
visited = [False] * (n+1)

def dfs(v):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        # i = 1
        s.append(i)
        dfs(i)
        s.pop()
dfs(1)