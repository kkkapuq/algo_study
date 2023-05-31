n = int(input())
nums = []
cnt = 0
for _ in range(n):
    n, c1, c2 = map(int, input().split())
    n = list(map(int, str(n)))
    # [첫째자리수, 둘째자리수, 셋째자리수, 카운트1, 카운트2] 형태로 입력 시켜놓는다.
    nums.append([n[0], n[1], n[2], c1, c2])

def ableYn(num):
    global nums
    for n in nums:
        cnt1, cnt2 = 0, 0
        # 1. 임의로 들어온 수 num이 위에서 주어진 조건을 다 만족하는지?
        for i in range(3):
            if n[i] == num[i]:
                cnt1 += 1
            elif n[i] != num[i] and num[i] in n[:3]:
                cnt2 += 1
        # 2. 만약 cnt1, cnt2가 위에서 설정한 값과 다르면 그 수는 유추 가능한 수가 될 수 없다.
        if cnt1 != n[3] or cnt2 != n[4]:
            return False
    return True

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or i == k or j == k:
                continue
            if ableYn([i, j, k]):
                cnt += 1

print(cnt)