'''
문제 : 안전지대
난이도 : 레벨 0
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120866
'''
'''
1. 단순 구현으로 할 수 있을것같긴함
2. 폭탄이 적용되는 인덱스별 예외 케이스를 정해보면 다음과 같다.
1) jndex를 중앙에 두고, 8개 방향에 위험지역 처리를 해주자
[i-1, j-1]  [i-1, j]    [i-1, j+1]
[i, j-1]    [i,j]       [i, j+1]
[i+1, j+1]  [i+1, j]    [i+1, j+1]
2) 이 친구들이 null이 아니라면 1로 만들어주고, 최종적으로 0의 개수를 return 하면 끝
'''

def solution(board):
    answer = 0
    n = len(board)
    # 결과 보드 선언
    safeboard = [ [0 for _ in range(n)] for _ in range(n)]
    n -= 1
    for index, i in enumerate(board):
        for jndex, j in enumerate(i):
            if j == 1:
                if not ((index-1 < 0 or index-1 > n) or (jndex-1 < 0 or jndex-1 > n)):
                    safeboard[index-1][jndex-1] = 1
                if not ((index-1 < 0 or index-1 > n) or (jndex < 0 or jndex > n)):
                    safeboard[index-1][jndex] = 1
                if not ((index-1 < 0 or index-1 > n) or (jndex+1 < 0 or jndex+1 > n)):
                    safeboard[index-1][jndex+1] = 1
                if not ((index < 0 or index > n) or (jndex-1 < 0 or jndex-1 > n)):
                    safeboard[index][jndex-1] = 1
                if not ((index < 0 or index > n) or (jndex < 0 or jndex > n)):
                    safeboard[index][jndex] = 1
                if not ((index < 0 or index > n) or (jndex+1 < 0 or jndex+1 > n)):
                    safeboard[index][jndex+1] = 1
                if not ((index+1 < 0 or index+1 > n) or (jndex-1 < 0 or jndex-1 > n)):
                    safeboard[index+1][jndex-1] = 1
                if not ((index+1 < 0 or index+1 > n) or (jndex < 0 or jndex > n)):
                    safeboard[index+1][jndex] = 1
                if not ((index+1 < 0 or index+1 > n) or (jndex+1 < 0 or jndex+1 > n)):
                    safeboard[index+1][jndex+1] = 1
    
    for i in safeboard:
        answer += i.count(0)

    return answer

solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]])