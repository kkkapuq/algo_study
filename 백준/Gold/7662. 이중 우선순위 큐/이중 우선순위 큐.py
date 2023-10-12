import sys
import heapq

t = int(input())

for i in range(t):
    k = int(input())
    
    # 최소값 힙과 최대값 힙 설정
    minHeap, maxHeap = [], []
    # 동기화 여부를 나타내기 위한 visited
    visited = [False] * 1000000
    
    for j in range(k):
        word, num = sys.stdin.readline().split()
        num = int(num)
        
        if word == 'I':
            # 삽입이면 힙큐에서 튜플 형태로 집어넣어준다. 
            # 최대 힙은 -num을 곱해주면 튜플의 첫번째 원소를 우선순위로 힙을 구성하게 된다. 일종의 테크닉이니 기억하자.
            heapq.heappush(minHeap, (num, j))
            heapq.heappush(maxHeap, (-num, j))
            visited[j] = True
        else:
            if num == 1:
                while maxHeap and not visited[maxHeap[0][1]]:
                    heapq.heappop(maxHeap)
                if maxHeap:
                    visited[maxHeap[0][1]] = False
                    heapq.heappop(maxHeap)
            else:
                while minHeap and not visited[minHeap[0][1]]:
                    heapq.heappop(minHeap)
                if minHeap:
                    visited[minHeap[0][1]] = False
                    heapq.heappop(minHeap)
    
    while minHeap and not visited[minHeap[0][1]]:
        heapq.heappop(minHeap)
    while maxHeap and not visited[maxHeap[0][1]]:
        heapq.heappop(maxHeap)
    
    if not minHeap or not maxHeap:
        print("EMPTY")
    else:
        maxNum = -maxHeap[0][0]
        minNum = minHeap[0][0]
        print(maxNum, minNum)
