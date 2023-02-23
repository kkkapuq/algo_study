'''
문제 : N과 M(6)
난이도 : 실버 3
링크 : https://www.acmicpc.net/problem/15655
'''

n, m = map(int, input().split())
sortedList = list(map(int, input().split()))

sortedList.sort()
s = []

def dfs(v):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(v, n):
        s.append(sortedList[i])
        dfs(v)
        s.pop()

dfs(0)