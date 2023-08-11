from collections import deque

def solution(q1, q2):
    answer = 0
    
    q1, q2 = deque(q1), deque(q2)
    sum1, sum2 = sum(q1), sum(q2)
    # 1. while문을 계속 돌면서, 두 수의 합이 같아질 때까지 돈다.
    while True:
        # 큰쪽에서 작은쪽으로 이동시켜준다.
        if sum1 > sum2:
            temp = q1.popleft()
            sum1 -= temp
            sum2 += temp
            answer += 1
            q2.append(temp)
        elif sum1 < sum2:
            temp = q2.popleft()
            sum1 += temp
            sum2 -= temp
            answer += 1
            q1.append(temp)
        else:
            break
        # q의 크기만큼 반복했는데 안된다는건 다 해봐도 안된다는 뜻임
        if answer == len(q1)*2:
            return -1
    
    return answer