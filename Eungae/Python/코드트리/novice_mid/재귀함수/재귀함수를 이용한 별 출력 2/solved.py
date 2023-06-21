def recursion(n):
    if n == 0:
        return
    temp = ['*' for _ in range(n)]
    print(' '.join(temp))
    recursion(n-1)

def recursion2(n):
    if n == 5:
        return
    temp = ['*' for _ in range(n)]
    print(' '.join(temp))
    recursion2(n+1)

n = int(input())
recursion(n)
recursion2(1)
