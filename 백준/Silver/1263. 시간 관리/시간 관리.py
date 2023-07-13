'''
문제 : 시간 관리
난이도 : 실버 1
링크 : https://www.acmicpc.net/problem/1263
'''
n = int(input())
arr = [ tuple(map(int, input().split())) for _ in range(n) ]

arr.sort(key=lambda x:x[1])
# 첫 시작시간을 가장 먼저 해야하는 일로 잡는다.
temp = arr[0][1] - arr[0][0]
if temp < 0:
    print(-1)
    exit()

while temp >= 0:
    start = temp
    flag = True
    # 만약 현재 시간에 일을 했는데 제시간안에 못끝낸다면 진행 불가 처리
    for t, e in arr:
        if start + t > e:
            flag = False
            break
        else:
            start += t
    # 진행 불가하다면 가능한 시간을 찾기위해 temp -= 1 해준다
    if not flag:
        temp -= 1
    # 현재 시간으로 진행이 가능하다면 현재 시간이 답이다.
    elif flag:
        break
print(temp)