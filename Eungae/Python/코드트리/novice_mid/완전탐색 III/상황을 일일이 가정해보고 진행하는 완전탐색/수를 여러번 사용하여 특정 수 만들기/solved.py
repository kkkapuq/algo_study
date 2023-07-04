a, b, c = map(int, input().split())

aArr = [a]
bArr = [b]

while True:
    if aArr[-1] + a <= c:
        aArr.append(aArr[-1] + a)
    if bArr[-1] + b <= c:
        bArr.append(bArr[-1] + b)

    if aArr[-1] + a > c and bArr[-1] + b > c:
        break
answer = 0


for i in aArr:
    for j in bArr:
        if i + j <= c:
            answer = max(answer, i+j)
    answer = max(answer, i)

for i in bArr:
    for j in aArr:
        if i + j <= c:
            answer = max(answer, i+j)
    answer = max(answer, j)
    
print(answer)