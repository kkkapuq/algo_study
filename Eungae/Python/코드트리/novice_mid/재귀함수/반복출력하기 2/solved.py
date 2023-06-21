n = int(input())

def recursion(n):
    if n == 0:
        return
    recursion(n-1)
    print('HelloWorld')

recursion(n)