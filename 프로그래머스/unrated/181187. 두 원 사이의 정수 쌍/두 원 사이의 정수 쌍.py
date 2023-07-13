'''
문제 : 요격 시스템
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181187
'''
import math

def solution(r1, r2):
    temp = 0
    # 1. 굳이 다 구할 필요 없다. 1사분면에 있는 사이에 정수만 구해서 *4 해준값 해주면됨
    # r1 == 2 and r2 가 아래와 같을 때 정수 쌍의 개수
    # 원점이 0, 0 인 원에서 x = i 일 때 y 값은 y**2 = r**2 - x**2
    # 따라서 y = sqrt(r**2 - x**2)
    
    # 3. 위 공식에 따라서, r2의 y값과 r1의 y값을 빼준 것에 int를 씌우면 점의개수가 도출된다.
    for x in range(r1):
        r1Y = math.sqrt(r1**2 - x**2)
        r2Y = math.sqrt(r2**2 - x**2)

        # # 3-1. 만약, r1Y, r2Y 값이 정수라면 이 부분에 대해서 예외 처리를 해줘야 한다.
        if int(r2Y) == r2Y or int(r1Y) == r1Y:
            if int(r2Y) == r2Y and int(r1Y) < r1Y:
                dots = int(r2Y) - int(r1Y)
            else:
                dots = int(r2Y) - int(r1Y) + 1
        else:
            dots = int(r2Y) - int(r1Y)
        temp += dots

    # 3-3. r1부터 r2까지 센다. 이 때, y=0인 좌표는 세지 않는다.
    for x in range(r1, r2):
        r2Y = int(math.sqrt(r2**2 - x**2))
        temp += r2Y
    
    return temp*4
print(solution(999, 1000))