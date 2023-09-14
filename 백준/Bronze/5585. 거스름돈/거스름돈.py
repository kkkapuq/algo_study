'''
문제 : 거스름돈
링크 : https://www.acmicpc.net/problem/5585
소요시간 : 15:16 ~ 
'''

n = int(input())
n = 1000 - n

cnt = 0

money, n = divmod(n, 1000)
cnt += money

money, n = divmod(n, 500)
cnt += money

money, n = divmod(n, 100)
cnt += money

money, n = divmod(n, 50)
cnt += money

money, n = divmod(n, 10)
cnt += money

money, n = divmod(n, 5)
cnt += money

money, n = divmod(n, 1)
cnt += money

print(cnt)