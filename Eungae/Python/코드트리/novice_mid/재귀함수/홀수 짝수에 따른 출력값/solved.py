n = int(input())

def recursion(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return recursion(n-2) + n

print(recursion(n))