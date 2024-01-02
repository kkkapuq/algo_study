from collections import deque

def solution(s):
    answer = 0
    
    n = len(s)
    
    for i in range(n):
        stack = deque(list(s))
        # n번 회전해주기
        for j in range(i):
            temp = stack.popleft()
            stack.append(temp)
        
        temp = []
        for j in stack:
            if temp:
                if j == ']' and temp[-1] == '[':
                    temp.pop()
                elif j == '}' and temp[-1] == '{':
                    temp.pop()
                elif j == ')' and temp[-1] == '(':
                    temp.pop()
                else:
                    temp.append(j)
            else:
                temp.append(j)
        if len(temp) == 0:
            answer += 1
    
    return answer