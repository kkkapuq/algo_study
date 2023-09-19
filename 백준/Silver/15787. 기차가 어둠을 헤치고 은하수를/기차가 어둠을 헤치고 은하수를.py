'''
문제 : 기차가 어둠을 헤치고 은하수를
링크 : https://www.acmicpc.net/problem/15787
소요시간 : 
'''
import sys
se = sys.stdin.readline
n, m = map(int, input().split())

train = [[False for _ in range(20)] for _ in range(n)]

for _ in range(m):
    inputlist = list(map(int, se().split()))
    order, num, seat = 0, 0, 0

    # 1, 2를 명령했을 때 변수 초기화
    if len(inputlist) == 3:
        order, num, seat = inputlist[0], inputlist[1], inputlist[2]
    else:
        order, num = inputlist[0], inputlist[1]

    # 인덱스 계산 편리하게 하기 위한 -1 작업
    num -= 1
    seat -= 1
    # 승차
    if order == 1:
        train[num][seat] = True
    # 하차
    elif order == 2:
        train[num][seat] = False
    # 뒤로 밀기
    elif order == 3:
        # 뒤로 밀어줘야 하므로, 뒤에서부터 탐색해야 당기기 용이해짐
        for i in range(19, -1, -1):
            # 만약 맨 뒷자리에 사람이 타고있으면 하차시킨다.
            if i == 19 and train[num][i]:
                train[num][i] = False
            else:
                # 만약 해당 자리에 사람이 타고있으면 뒤로 밀어준다.
                if train[num][i]:
                    train[num][i+1] = True
                    train[num][i] = False
    # 앞으로 당기기
    elif order == 4:
        for i in range(20):
            # 만약 맨 앞자리에 사람이 타고있으면 하차시킨다.
            if i == 0 and train[num][i]:
                train[num][i] = False
            else:
                # 만약 해당 자리에 사람이 타고있으면 앞으로 당겨준다.
                if train[num][i]:
                    train[num][i-1] = True
                    train[num][i] = False 

# 중복된 기차가 있다면, 하나만 통과 가능하다, set해주자
# 중복을 제거해줄 set
tempSet = set()
for i in train:
    tempSet.add(tuple(i))

# 이 set의 길이가 정답
print(len(tempSet))