'''
문제 : 카드 합체 놀이
링크 : https://www.acmicpc.net/problem/15903
소요시간 : 18:20 ~ 18:40
'''
n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    arr.sort()

    arr[0], arr[1] = arr[0]+arr[1], arr[0]+arr[1]

print(sum(arr))