import sys
from itertools import product

si = sys.stdin.readline


def solution():
    n, m = map(int, si().split())
    nums = sorted(map(int, si().split()))
    return '\n'.join(map(' '.join, product(map(str, nums), repeat=m)))


print(solution())
