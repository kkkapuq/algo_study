'''

'''
def solution(n):
    cntN = format(n, 'b').count('1')
    print(cntN)
    
    for i in range(n+1, 1000001):
        cntI = format(i, 'b').count('1')
        if cntI == cntN:
            return i
    