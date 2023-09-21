'''
문제 : 사다리 타기
링크 : https://www.acmicpc.net/problem/2469
소요시간 : failed
'''
import sys
se = sys.stdin.readline
k = int(input())
n = int(input())
end = list(input())
# 아이디어, 첫 start를 정렬시켜버리면 복잡한 로직이 필요없다.
start = sorted(end)

ladder = [list(se().rstrip()) for _ in range(n)]

ladderA, ladderB = [], []

# ??? 가 나오기 전과 후를 나눠준다.
for i in range(n):
    if ladder[i][0] == '?':
        ladderA = ladder[:i]
        ladderB = ladder[i+1:]
        break

# ??? 가 나오기 전까지 사다리를 타고 내려가며 start를 변경해준다.
for i in ladderA:
    for j in range(k-1):
        if i[j] == '-':
            start[j], start[j+1] = start[j+1], start[j]

# ??? 가 나온 후의 사다리를 역순으로 타고 올라오면서, end를 변경해준다.
ladderB.reverse()
for i in ladderB:
    for j in range(k-1):
        if i[j] == '-':
            end[j], end[j+1] = end[j+1], end[j]

# 이렇게 정리된 두 start, end 배열을 비교하면서 사다리를 만들어주면 끝
answer = []
for i in range(k-1):
    if start[i] == end[i]:
        answer.append('*')
    else:
        # 사다리를 위에서 타고 내려오면서 왼쪽 -> 오른쪽으로 가서 바뀐경우
        if start[i] == end[i+1]:
            answer.append('-')
        # 사다리를 위에서 타고 내려오면서 오른쪽 -> 왼쪽으로 가서 바뀐경우
        elif i!=0 and start[i]==end[i-1]:
            answer.append("*")
        else:
            answer = ['x' for _ in range(k-1)]
            break

print(''.join(answer))