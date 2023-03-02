import sys
sys.setrecursionlimit(int(1e8))
input = sys.stdin.readline

n, m = map(int, input().strip().split())

# def rec(idx, used, nums):
#     # 인자 설명
#     # idx: 처음 시작하는 숫자(네이밍 미숙)
#     # used: 지금까지 사용한 숫자의 개수
#     # nums: 지금까지 사용한 숫자들을 저장하는 배열 
#     if used == m:
#         print(*nums)
#         return
#     for i in range(idx+1, n+1):
#         nums.append(i)
#         rec(i, used+1, nums)
#         nums.pop()

# # 1부터 시작해서 뒤에서부터 m번째까지 적용 
# for i in range(1, n-m+2):
#     rec(i, 1, [i])