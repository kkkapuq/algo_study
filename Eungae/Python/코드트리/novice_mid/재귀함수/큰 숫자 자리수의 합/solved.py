def recursion(n):
    if n < 10:
        return n
    temp = int('1'.ljust(len(str(n)), '0'))
    return n//temp + recursion(n%temp)

a, b, c = map(int, input().split())
print(recursion(a*b*c))

# temp = '1'.rjust(3, '0')
# print(temp)