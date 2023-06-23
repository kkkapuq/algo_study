def recursion(n):
    global answer
    if n == 1:
        return
    if n % 2 == 0:
        answer += 1
        return recursion(n/2)
    elif n %  2 != 0:
        answer += 1
        return recursion(n*3+1)
    
n = int(input())
answer = 0
recursion(n)
print(answer)
