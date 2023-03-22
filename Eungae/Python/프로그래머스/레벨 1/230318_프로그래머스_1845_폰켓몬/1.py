'''
문제 : 폰켓몬
난이도 : 레벨 1
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/1845
'''
'''
1. combinations 사용하기
2. combinations 사용해서 나온 결과들을 for문을 돌면서 맵을 활용해 비교해주기
3. 최종 max값 도출
4. 시간복잡도는 3^n ?
'''
from itertools import combinations

'''
# 틀린 풀이
def solution(nums):
    n = len(nums) / 2
    
    combList = list(combinations(nums, 3))
    maxNum = 0
    print(combList)
    
    for i in combList:
        temp = {}
        for j in i:
            if j not in temp:
                temp[j] = True
        maxNum = max(maxNum, len(temp))
    
    return maxNum
'''

'''
# 틀린 풀이
def solution(nums):
    n = len(nums) // 2
    
    combList = list(combinations(nums, n))
    maxNum = 0
    
    for i in combList:
        i = set(i)
        maxNum = max(maxNum, len(i))
    
    return maxNum
'''

'''
0. 어쨋든 정답은 n이하여야됨, 왜? n개 포켓몬을 골랐는데 n개 초과로 뽑힐 수는 없으니까.
1. 중복을 제거한게 n과 무관하게 나올 수 있는 최대 조합의 수임 이걸 k라고 가정하자
2. 그래서 k가 n보다 작으면 그냥 k값 return 해주는거고 n보다 크거나 같으면 n개의 종류를 고를 수 있는거니까 n return 하는거임
'''
def solution(nums):
    n = len(nums) // 2
    maxLen = 0

    nums = set(nums)
    if n < len(nums):
        maxLen = n
    else:
        maxLen = len(nums)
    
    return maxLen

solution([3,3,3,2,2,4])