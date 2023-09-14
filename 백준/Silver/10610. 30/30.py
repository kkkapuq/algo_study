'''
문제 : 30
링크 : https://www.acmicpc.net/problem/10610
소요시간 : 15:30~
'''
n = list(input())

n.sort(reverse=True)
n = int(''.join(n))
n = n if n % 30 == 0 else -1
print(n)