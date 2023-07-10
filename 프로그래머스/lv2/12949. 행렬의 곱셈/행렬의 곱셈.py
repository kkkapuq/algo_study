'''
문제 : 행렬의 곱셈
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12949
'''
def solution(arr1, arr2):
    answer = []
    
    # arr1의 행, 열, arr2의 행, 열
    lc, lr, rc, rr = len(arr1), len(arr1[0]), len(arr2), len(arr2[0])
    # 결과는 lc x rr 의 크기를 가진 행렬
    
    for i in range(lc):
        tempArr = []
        for j in range(rr):
            temp = 0
            for k in range(lr):
                temp += arr1[i][k] * arr2[k][j]
            tempArr.append(temp)
        answer.append(tempArr)
            
    return answer