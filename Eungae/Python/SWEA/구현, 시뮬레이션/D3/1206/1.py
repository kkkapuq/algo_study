'''
문제 : [S/W 문제해결 기본] 1일차 - View
난이도 : D3
링크 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=1206&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
'''
'''
1. 현재 높이 - 양 옆 2칸중에 가장 높은 칸 더해주면 끝
'''
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    buildings = list(map(int, input().split()))
    cnt = 0
    # 범위 탐색
    for i, height in enumerate(buildings):
        if i < 2 or i > N-2 or height == 0:
            continue
        # 양옆 2칸중에 가장 높은 칸 저장하기
        maxheight = max(buildings[i-1], buildings[i-2], buildings[i+1], buildings[i+2])
        if height > maxheight:
            cnt += height - maxheight
     
    print('#' + str(test_case) + ' ' + str(cnt))