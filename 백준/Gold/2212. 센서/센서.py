'''
문제 : 센서
링크 : https://www.acmicpc.net/problem/2212
소요시간 : 18:45~
'''
n = int(input())
k = int(input())
arr = list(map(int, input().split()))

# 계산의 편의를 위해 정렬한다.
arr.sort()

# 만약 센서 갯수보다 집중국이 같거나 많다면, 걍 센서마다 하나씩 놔주면 되니까 0 출력하고 종료
if k >= n:
    print(0)
    exit()


# i부터 i+1번째 센서까지의 거리를 저장한다. 이후 내림차순으로 정렬해준다.
dist = []
for i in range(n-1):
    dist.append(arr[i+1] - arr[i])

dist.sort(reverse=True)

# 최소한의 거리만 구하면 된다, 따라서 집중국의 수 만큼 앞에서 인덱스를 제거해주자.
for i in range(k-1):
    dist.pop(0)

# 남아있는 거리들의 합이 집중국이 커버할 수 있는 총 거리이다.
print(sum(dist))