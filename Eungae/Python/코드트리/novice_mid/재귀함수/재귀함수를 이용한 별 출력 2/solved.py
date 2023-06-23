def recursion(n):
    if n == 0:
        return
    temp = ['*' for _ in range(n)]
    print(' '.join(temp))
    recursion(n-1)

def recursion2(a):
    global n
    if a == n+1:
        return
    temp = ['*' for _ in range(a)]
    print(' '.join(temp))
    recursion2(a+1)

n = int(input())
recursion(n)
recursion2(1)
