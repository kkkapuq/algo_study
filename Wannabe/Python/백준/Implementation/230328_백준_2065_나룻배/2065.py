from collections import deque
import sys

si = sys.stdin.readline

capa, ttime, m = map(int, si().strip().split())
ms = [si().strip().split() for _ in range(m)]
ms = deque([[i, int(o[0]), o[1]] for i, o in enumerate(ms)])
side, current = 'left', 0
left = deque([])
right = deque([])
boat = deque([])
res = [0]*m
cnt = 0
# 현재 위치에 손님이 있는지 판단
# 1. 있으면 M명을 태운다
# 2. 없으면
    #  2-1. 현재시점에 있는 정박장에 손님이 없으면 정박장 가장 앞에 올 손님쪽을 내보내는 시점으로 현재시점 업데이트
        # 2-1-1. 현재시점 업데이트 된곳에 손님이라면 태우고
        # 2-1-2. 현재시점 업데이트 된곳의 반대쪽 손님이라면
# 3. 반대쪽으로 이동한다 (즉 1-3, 1-2를 반복)

def update_slot(time, passengers):
    # 시간에 따라서 left, right side를 업데이트 하는 함수
    # 지금은 left right는 global (나중에 인자로)
    while passengers:
        t, arr_time, side = passengers.popleft()
        if int(arr_time) > time:
            passengers.appendleft([t, arr_time, side])
            return
        else:
            if side == 'left':
                left.append(t)
            else:
                right.append(t)
while cnt < m:
    # 내가 지금 있는 위치에 손님이 있다는 걸 어떻게 표현하지? side는 왜만들었지?
    # 문제에서 준 승객리스트를 가지고 1. 먼저 left right 를 채울건지, 아니면 2. 시점에 따라서 left right를 업데이트 할건지 정해
    # 2를 선택 -> 그럼 시점이랑 승객리스트가 주어지면 left, right를 채우는 함수를 만든다

    # 현재 시점의 내 위치는 ? cur_time은 0이니까 다음 시점이 언젠지 알아야된다.
    # 다음시점은 손님이 어딘가에 왔을 시점이다. 현재시간과 손님리스트를 넣어준다
        # 예를들면 처음엔 0분
        # 그럼에도 불구하고 손님이 하나도 없다. 그럼 손님오는 시점으로 업데이트한다.

    update_slot(current, ms)

    if side == 'left':                 # 현재 내가 왼쪽에 있고 탑승객이 존재하면
        while len(boat) < capa and left:                 # capa가 다채워질때까지 손님을 받는다. left 배열이니까 오른쪽으로 가고싶은 사람들
            # 태워서 가는 사람들에 대한 정보
            boat.append(left.popleft())
        if not left and not right and not boat and ms:                    # 탑승객이 존재하지 않을때
            # 대기
            current = ms[0][1]

            update_slot(current, ms)
            while len(boat) < capa and left:
                boat.append(left.popleft())
    else:                               # 현재 내가 오른쪽에 있고 탑승객이 존재하면
        while len(boat) < capa and right:
            boat.append(right.popleft())

        if not left and not right and not boat and ms:  # 탑승객이 존재하지 않을때
            # 대기
            current = ms[0][1]

            update_slot(current, ms)
            while len(boat) < capa and right:
                boat.append(right.popleft())
    current += ttime
    side = 'right' if side == 'left' else 'left'

    while boat:
        res[boat.popleft()] = current
        cnt += 1
    print(*ms)

print('----')
print(*res, sep='\n')
"""
2 10 3
10 right
25 left
40 left
"""