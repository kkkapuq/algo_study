'''
문제 : 더 맵게
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42626
'''
import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    while len(scoville) > 1:
        a, b = heapq.heappop(scoville), heapq.heappop(scoville)
        if a >= K:
            return answer 
        heapq.heappush(scoville, a + (b*2))
        answer += 1
        
    if scoville[0] < K:
        return -1
        
    return answer