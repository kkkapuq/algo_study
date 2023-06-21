def recursion(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return recursion(n-2) + recursion(n-1)
    

n = int(input())
print(recursion(n))