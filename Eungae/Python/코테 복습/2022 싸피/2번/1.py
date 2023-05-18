'''
2번
N개의 바구니가 있고, 각 바구니마다 사과가 있을수도 있고 없을수도 있다.
사과를 먹는 벌레를 특정 위치에 놓아주고 싶다.
벌레는 매 순간 자기와 가장 가까운 위치로 이동해서 사과를 먹기 시작한다.

이 벌레가 가장 가까이 있는 사과가 2개 이상이 될 때 뭘 먹어야할지 몰라서 죽어버린다.
X라는 별도의 값이 입력되고, 벌레가 죽지않고 모든 사과를 먹을 수 있는 시작점 중에서 가장 가까운 위치를 출력해라.

1 <= N <= 300
'''
'''
1. 특정 시작지점이 s라고 치면, 양쪽을 탐색해 나가며 사과가 나올 때까지
'''
N, X = map(int, input().split())
a = list(map(int, input().split()))

def solve(start: int) -> bool:
    # 이전 TC에서 먹었다고 표현한(2) 것을 다시 1로 돌려주는 작업
    for i in range(N):
        if a[i] == 2:
            a[i] == 1
    # start에서 시작했을 떄, 모든 사과를 먹을 수 있는가?
    cur = start
    while True:
        # 1. 가장 가까운 사과까지의 거리 계산
        min_dist = N + 1
        for i in range(N):
            if a[i] == 1:
                min_dist = min(min_dist, abs(i - cur))
        # 2. 없다면, 모든 사과를 먹었으므로 해결
        if min_dist == N + 1:
            return True

        # 3. 이동 선택지가 두 가지라면 불가능하다고 판단
        left = cur - min_dist
        right = cur + min_dist
        if (0 <= left and a[left] == 1) and (right < N and a[right] == 1):
            return False

        # 4. 한 가지 뿐이라면, 해당 위치로 이동해서 사과를 먹기
        if (0 <= left and a[left] == 1):
            cur = left
            a[cur] = 2
        else:
            cur = right
            a[cur] = 2

X -= 1
for d in range(N): # X와의 거리가 d인 두 위치를 확인하자.
    if X - d >= 0 and solve(X - d): # 왼쪽으로 d만큼 떨어진 X - d 위치
        print(d)
        break
    if X + d < N and solve(X + d): # 오른쪽으로 d만큼 떨어진 X + d 위치
        print(d)
        break
