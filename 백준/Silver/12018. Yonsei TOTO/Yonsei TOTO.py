'''
문제 : Yonsei TOTO
링크 : https://www.acmicpc.net/problem/12018
소요시간 : 16:10 ~ 
'''
n, m = map(int, input().split())
cnt = 0

# 강의별 듣기위한 최소 마일리지로 이루어진 arr
mile = []
for _ in range(n):
    p, l = map(int, input().split())
    # 해당 강의를 듣기 위한 최소 마일리지
    temp = list(map(int, input().split()))
    # 마일리지를 많이 쓴 사람순으로 정렬
    temp.sort(reverse=True)
    # 만약 수강인원보다 많이 신청한 상태라면, 딱 n번째 순위 사람만큼만 넣으면 우선순위가 나한테 있어서 수강이 가능해진다.
    if p >= l:
        mile.append(temp[l-1])
    else:
        # 신청인원이 수강인원보다 적다면, 그냥 1만 넣어도 수강이 가능해진다.
        mile.append(1)

# 강의별 최소 마일리지를 오름차순 정렬해준다.
mile.sort()

for i in mile:
    if m - i >= 0:
        cnt += 1
        m -= i
    else:
        break

print(cnt)
