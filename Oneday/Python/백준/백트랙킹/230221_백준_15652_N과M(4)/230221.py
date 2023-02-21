'''
신규_백준_15651_N과M(4)
-백트래킹
-첫 풀이

문제 : N과 M(4)
난이도 : 실버 3
링크 : https://www.acmicpc.net/problem/15652

풀이방법
- 지난 번과 풀이 방법은 똑같아서 외워서 풀었다.
- 조건 하나만 추가.
'''
n, m = map(int,input().split())
s = []

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n+1):
        if start <= i:
           s.append(i)
           dfs(i)
           s.pop()

dfs(1)