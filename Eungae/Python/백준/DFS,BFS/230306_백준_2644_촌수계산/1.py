'''
문제 : 촌수계산
난이도 : 실버 2
링크 : 
'''
'''
- 문제요약
1. 관계의 개수 m이 있음
2. a와 b간의 촌수 거리를 구하기
3. 촌수가 전혀 없으면 -1

- 아이디어
1. a부터 dfs를 도는데, i번째 사람이랑 몇촌인지를 나타내는 people을 선언해주기
2. graph에 관계를 담아두고, visited에 방문하지 않았으면 촌수를 늘려서 people[i]에 저장해주기
3. 마지막에 people[b]가 0보다 크면 people[b]를 return, 아니라면 -1 해주기
'''
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            people[i] = people[v] + 1
            dfs(i)

n=int(input())
a,b=map(int,input().split())
m=int(input())

graph=[[] for _ in range(n+1)]
visited = [False] * (n+1)
people=[0]*(n+1)

for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(a)

if people[b]>0:
    print(people[b])
else:
    print(-1)