'''
문제 : [S/W 문제해결 기본] 1일차 - Flatten
난이도 : D3
링크 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh&categoryId=AV139KOaABgCFAYh&categoryType=CODE&problemTitle=1208&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
'''
'''
1. 가장 높은박스와 낮은 박스 구해서, 해당 인덱스 +- 해주면 됨.
'''

T = int(input())

for test_case in range(1, T + 1):
    dump = int(input())
    boxes = list(map(int, input().split()))
    for i in range(dump):
        maximum = max(boxes)
        minimum = min(boxes)
        boxes[boxes.index(maximum)] -= 1
        boxes[boxes.index(minimum)] += 1

    print('#' + str(test_case) + ' ' + str(max(boxes) - min(boxes)))