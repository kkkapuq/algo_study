'''
문제 : 숫자 배열 회전
난이도 : D2
링크 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq
'''
'''
1. 회전별로 어떤 인덱스가 어디로 들어가야되는지 규칙을 찾으면 쉽다.
2. 공간복잡도를 줄일 수 있는 방법이...있나?
'''

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    square = [ list(map(int, input().split())) for _ in range(N) ]
    # 각각 90도, 180도, 270도 회전한 모양
    first, second, third =   [ [ 0 for _ in range(N) ] for _ in range(N) ], [ [ 0 for _ in range(N) ] for _ in range(N) ], [ [ 0 for _ in range(N) ] for _ in range(N) ]
    
    # 회전한 사각형을 for문마다 저장
    for i in range(N):
        for j in range(N):
            first[i][j] = square[N-1-j][i]
            second[i][j] = square[N-1-i][N-1-j]
            third[i][j] = square[j][N-1-i]
    
    # 정답 출력
    print('#' + str(test_case))
    for i in range(N):
        print(''.join(map(str, first[i])) + ' ' + ''.join(map(str, second[i])) + ' ' + ''.join(map(str, (third[i]))))
            