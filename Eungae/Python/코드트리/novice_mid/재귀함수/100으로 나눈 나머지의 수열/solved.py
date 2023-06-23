n = int(input())

def recursion(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4
    else:
        return (recursion(n-2)*recursion(n-1)) % 100

print(recursion(n))