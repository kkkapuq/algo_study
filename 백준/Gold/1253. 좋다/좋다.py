'''
문제 : 좋다
난이도 : 골드 4
링크 : https://www.acmicpc.net/problem/1253
소요시간 : 
'''
import sys
import heapq
se = sys.stdin.readline
n = int(se().rstrip())
answer = 0

heap = list(map(int, se().split()))
# heapq.heapify(heap) 이거 쓰면 정렬이안됨.. 왜?
heap.sort()

for i in range(n):
    # 대상 숫자보다 적은 수들로 리스트를 구성하고, 그 리스트 안에서 투포인터로 돌면서 좋은 수가 되는지 판별한다.
    arr = heap[:i] + heap[i+1:]
    start = 0
    end = len(arr)-1
    while start < end:
        temp = arr[start] + arr[end]
        if temp == heap[i]:
            answer += 1
            break
        # 만약 이 수 비교하고자 하는 수보다 크면, 오른쪽 값을 줄여줘야 한다.
        if temp > heap[i]:
            end -= 1
        else:
            # 아니라면 왼쪽 값 늘려주기
            start += 1

print(answer)