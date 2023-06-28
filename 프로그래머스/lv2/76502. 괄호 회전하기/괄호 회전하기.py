def solution(s):
    answer = 0
    s = list(s)
    for i in range(len(s)):
        stack = []
        for j in range(len(s)):
            if stack:
                if (s[j] == ']' and stack[-1] == '[') or \
                    (s[j] == '}' and stack[-1] == '{') or \
                    (s[j] == ')' and stack[-1] == '('):
                    stack.pop()
                else:
                    stack.append(s[j])
            else:
                stack.append(s[j])
        if not stack:
            answer += 1
        temp = s.pop(0)
        s.append(temp)
    
    return answer