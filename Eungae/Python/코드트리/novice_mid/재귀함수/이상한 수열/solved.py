n = int(input())

def recursion(n):
    if n == 1: 
        return 1
    if n == 2:
        return 2
    else:
        num = int(n/3)
        return recursion(num) + recursion(n-1)

print(recursion(n))