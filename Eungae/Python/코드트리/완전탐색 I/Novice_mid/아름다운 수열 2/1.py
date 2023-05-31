from itertools import combinations, permutations
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

beautifuls = list(permutations(b, m))

def isbeautiful(arr):
    global beautifuls

    if arr in beautifuls:
        return True
    
    return False

cnt = 0
n = len(a)
for i in range(n-2):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if isbeautiful((i, j, k)):
                cnt += 1

print(cnt)