from collections import deque


def solution(numbers, target):
    answer = 0

    # search nxt node by adding or subtracting next element in numbers
    # search strategy: bfs
    # bfs time complexity - 2**20 =1000000 , let's try
    def bfs(idx):
        nonlocal numbers, target, answer
        length = len(numbers)
        q = deque([(numbers[idx], idx), (-numbers[idx], idx)])
        while q:
            nxt, id = q.popleft()
            if id == len(numbers) - 1 and nxt == target:
                answer += 1
            if id + 1 < length:
                q.append((nxt + numbers[id + 1], id + 1))
                q.append((nxt - numbers[id + 1], id + 1))

    bfs(0)
    return answer
