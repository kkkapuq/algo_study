n = int(input())

def recursion(n):
    if n < 10:
        return n*n
    return recursion(n//10) + recursion(n%10)

print(recursion(n))