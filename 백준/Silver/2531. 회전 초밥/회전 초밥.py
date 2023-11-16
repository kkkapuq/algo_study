import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().rstrip().split())
sushi = [int(input()) for _ in range(N)]
max_number_of_type = 0
for i in range(N):
    if i+k > N:
        number_of_type = len(set(sushi[i:N] + sushi[:(i+k)%N] + [c]))
    else:
        number_of_type = len(set(sushi[i:i+k] + [c]))
    if max_number_of_type < number_of_type:
        max_number_of_type = number_of_type
print(max_number_of_type)