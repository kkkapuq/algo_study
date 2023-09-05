n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

#단지의 세대 수
nums = []
count = 0

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False


for i in range(n):
    for j in range(n):
        # 모임인 집이 존재한다면
        if dfs(i, j) == True:
            nums.append(count)
            count = 0

nums.sort()
print(len(nums))
for i in nums:
    print(i)