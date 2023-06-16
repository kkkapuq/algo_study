import sys, copy
a = list(input())
answer = -sys.maxsize

for i in range(len(a)):
    temp = copy.deepcopy(a)
    if temp[i] == '0':
        temp[i] = '1'
    elif temp[i] == '1':
        temp[i] = '0'
    
    # 2진수를 10진수로 변환해주고 최대값 탐색
    temp = int(''.join(temp), 2)
    answer = max(temp, answer)

print(answer)