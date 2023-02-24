import math
def cnt_num(n):
    cnt = 0
    # cnt until sqrt and *2
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            cnt += 2
            if i**2 == n:
                cnt -= 1
    return cnt
def solution(number, limit, power):
    # 1.common factor's #
    # 2. from 1, check if it's less than limit
    # 3. if it's greater than limit, assign power
    # iterate 1-3 for number' times     
    answer = 0
    for i in range(1, number+1):
        pos = cnt_num(i)
        if pos > limit:
            pos = power
        answer += pos
    return answer