import sys
se = sys.stdin.readline

n, m, k = map(int, se().split())
scores = list(map(int, se().split()))
yuts = []
positions = []

answer = 0

def calc():
    global answer
    positions = [1 for i in range(len(yuts))]
    temp = 0
    for idx, i in enumerate(yuts):
        positions[i-1] += scores[idx]
        if positions[i-1] == m:
            temp += 1
    answer = max(answer, temp)

def recursion(cnt):
    if cnt == n:
        calc()
        return

    for i in range(k):
        yuts.append(i)
        recursion(cnt+1)
        yuts.pop()


recursion(0)
print(answer)