'''
문제 : 파일정리
링크 : https://www.acmicpc.net/problem/20291
소요시간 : 
'''
import sys
from collections import defaultdict
se = sys.stdin.readline

n = int(input())
files = defaultdict(int)

for _ in range(n):
    name, extention = se().strip().split('.')

    files[extention] += 1

sortedFiles = sorted(files.items(), key=lambda x:x[0])

for i in sortedFiles:
    print(i[0], end=' ')
    print(i[1])