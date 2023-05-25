n = int(input())
arr = list(map(int, input().split()))

cnt = 0

for i in range(n):
    temp = [arr[i]]
    for j in range(i, n):
        # 같은 구간은 하나만 넣으면됨
        if i != j:
            temp.append(arr[j])
        avg = sum(temp) / len(temp)
        if avg in temp:
            cnt += 1
print(cnt)