'''
문제 : N과 M(5)
난이도 : 실버 3
링크 : https://www.acmicpc.net/problem/15654
'''

n, m = map(int, input().split())
sortedList = list(map(int, input().split()))

sortedList.sort()
visited = [False] * n
out = []

def dfs(depth, n, m):
    if depth == m:
        print(' '.join(map(str, out)))
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            out.append(sortedList[i])
            solve(depth+1, n, m)
            out.pop()
            visited[i] = False

dfs(0, n, m)