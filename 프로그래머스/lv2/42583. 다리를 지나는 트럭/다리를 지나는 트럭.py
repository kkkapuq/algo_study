'''
문제 : 다리를 건너는 트럭
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42583
'''
from collections import deque

def solution(bridgeLength, weight, truckWeights):
    answer = 0
    # 다리를 건넌 트럭들
    complete = []
    
    n = len(truckWeights)
    truckWeights = deque(truckWeights)

    # 시초나서 sum 대신 변수로 활용
    currentWeight = 0
    
    # 다리 역할을 하는 큐
    bridge = deque([0] * bridgeLength)
    
    # 초단위로 계속 작업을 수행한다.
    while True:
        if len(complete) == n:
            break
        answer += 1
        
        # 하나를 pop해주고, 나중에 append 하는 식으로 구성하자.
        # 계속 밀리고 사라지고 하는 구조기 때문
        t = bridge.popleft()
        if t != 0:
            complete.append(t)
            currentWeight -= t
        
        # 현재 다리를 체크한다.
        if len(truckWeights) > 0:
            if currentWeight + truckWeights[0] <= weight:
                truck = truckWeights.popleft()
                bridge.append(truck)
                currentWeight += truck
            else:
                # 앞에서 pop을 미리 해줬으니까 트럭이 더 못들어오는 경우는 append를 해줘서 기존 트럭을 앞으로 옮겨주는 작업을 수행
                bridge.append(0)
            
        
    return answer