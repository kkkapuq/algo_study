'''
문제 : 농작물 수확하기
난이도 : D3
링크 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB
'''
'''
1. i가 N//2보다 작을때, 같을때, 클때로 구분하자.
2. 규칙별로 더해주면 끝
'''
'''
# 최적화되지 않은 풀이
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    farm = [ list(map(int, input())) for _ in range(N) ]
    cnt = 0

    for i in range(N):
        for j in range(N):
            # 1. i < N // 2 일때
            if i < N//2:
                if j >= N//2-i and j <=N//2+i:
                    cnt += farm[i][j]
            # 2. i == N // 2 일때
            if i == N//2:
                cnt += farm[i][j]
            # 3. i > N // 2 일때
            if i > N//2:
                if j >= i-(N//2) and j <= (N//2) + abs(i-N+1):
                    cnt += farm[i][j]
    
    print('#' + str(test_case) + ' ' + str(cnt))
'''

# 최적화 풀이, 맨해튼 거리 사용
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    farm = [ list(map(int, input())) for _ in range(N) ]
    cnt = 0
    center = N//2

    for i in range(N):
        for j in range(N):
            # 1. 중간지점에서 가장 먼 곳 까지의 거리는 최대 N//2 니까, 그 이하인 애들은 모두 마름모 영역에 해당된다.
            if abs(center - i) + abs(center - j) <= N//2:
                cnt += farm[i][j]
    
    print(f'#{test_case} {cnt}')