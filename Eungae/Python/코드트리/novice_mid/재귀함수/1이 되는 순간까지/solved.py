n = int(input())
def recursion(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return recursion(n//2)+1
    else:
        return recursion(n//3)+1

print(recursion(n))