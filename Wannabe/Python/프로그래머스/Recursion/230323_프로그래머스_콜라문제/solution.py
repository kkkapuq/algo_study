import sys
sys.setrecursionlimit(int(1e6))
def solution(a, b, n):
    answer = 0
    def helper(a, b, n):
        nonlocal answer
        if a > n:   return 0
        answer += n//a*b
        return helper(a, b, n//a*b+n%a)
    helper(a, b, n)
    return answer