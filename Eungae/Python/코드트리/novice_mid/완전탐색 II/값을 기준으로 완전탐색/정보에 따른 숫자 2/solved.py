t, a, b = map(int,input().split())

sLine, nLine = [], []
answer = 0
for _ in range(t):
    word, index = input().split()
    if word == 'S':
        sLine.append(int(index))
    if word == 'N':
        nLine.append(int(index))
        
def minDistance(line, point):
    d = 9999
    for i in line:
        d = min(d, abs(i - point))
    return d

for i in range(a, b+1):
    ds, dn = minDistance(sLine, i), minDistance(nLine, i)
    if ds <= dn:
        answer += 1

print(answer)
