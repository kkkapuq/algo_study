def solution(numbers):
    answer = []
    
    '''
    2 - 3
    3 - 5
    5 - 6
    7 - 11
    8 - 9
    9 - 10
    10 - 11
    11 - 13
    12 - 13
    13 - 14 - 1101, 1110
    14 - 15
    15 - 23 - 01111, 10111
    16 - 17
    17 - 18 - 10001, 10010
    18 - 19
    '''
    # 2진수 자리수가 추가될 때마다 변화가 커짐.
    # 2^n-1 의 숫자들이 해당 숫자들임
    # 최대 2개의 비트만 바꿔야함
    # 짝수는 뒤에 1만 붙이면 됨
    # 홀수는 가장 마지막 자리의 0을 1로 바꿔주고, 그 다음 자리의 1을 0으로 바꿔주면됨
    
    for num in numbers:
        # 1. 계산상의 편의를 위해 앞에 '0'을 붙여서 계산한다.
        temp = list('0' + format(num, 'b'))
        if num % 2 == 0:
            answer.append(num+1)
        else:
            idx = 0
            # 2. 뒷자리의 0을 찾는 과정
            for i in range(len(temp)-1, -1, -1):
                if temp[i] == '0':
                    temp[i] = '1'
                    idx = i
                    break
            # 3. 뒷자리 0부터 가장 가까운 1을 찾는 과정
            for i in range(idx+1, len(temp)):
                if temp[i] == '1':
                    temp[i] = '0'
                    break
            answer.append(int(''.join(temp), 2))
    
    return answer