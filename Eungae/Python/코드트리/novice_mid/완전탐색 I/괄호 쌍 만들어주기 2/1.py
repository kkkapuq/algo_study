words = list(input())
n = len(words)
cnt = 0

for i in range(n-1):
    if words[i] == '(' and words[i+1] == '(':
        for j in range(i+2, n-1):
            if words[j] == ')' and words[j+1] == ')':
                cnt += 1

print(cnt)