import sys

si = sys.stdin.readline

# n l
N, L = map(int, si().strip().split())
# grid
grid = [list(map(int, si().strip().split())) for _ in range(N)]


def valid_vector(arr):
    l, r = 0, 0
    while r < N:
        if arr[l] != arr[r]:
            diff = abs(arr[r] - arr[l])
            if diff > 1:
                return False
            if arr[r] != arr[r-1]:
                l = r-1
            width = abs(r - l)
            if width < L:
                if r == N - 1 or arr[r] != arr[r + 1] or (arr[r] > arr[l] and arr[r] == arr[r+1]):
                    return False
            else:
                l = r
        r += 1
    return True


ans = 0
for i in range(N):  # row vector examination
    if valid_vector(grid[i]):
        print(*grid[i])
        ans += 1

for i in range(N):
    col = []
    for j in range(N):
        col.append(grid[j][i])
    if valid_vector(col):
        print(*col)
        ans += 1

print(ans)

"""
3 3 3 3 3 3
1 1 1 2 2 2
3 2 2 1 1 1
"""