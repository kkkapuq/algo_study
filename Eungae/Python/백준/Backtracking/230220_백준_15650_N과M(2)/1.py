'''
문제 : N과 M(2)
난이도 : 실버 3
링크 : https://www.acmicpc.net/problem/15650
'''
'''
1. s == m일 때, 오름차순이 아닌것만 체크하자
'''

n, m = map(int, input().split())
visited = [False] * (n+1)
s = []

def dfs(v):
    if len(s) == m:
        # 오름차순 정렬이 아닌 수열은 건너뛴다.
        isAsc = True
        for i in range(len(s)-1):
            if s[i] >= s[i+1]:
                isAsc = False
                break
        if isAsc:
            print(' '.join(map(str, s)))
            return
    else:
        # 백트래킹 과정
        for i in range(v, n+1):
            if not visited[i]:
                visited[i] = True
                s.append(i)
                dfs(i)
                s.pop()
                visited[i] = False
            
    
dfs(1)