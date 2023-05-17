'''
1. 교환 횟수를 모두 소진해야한다.
2. 따라서 현재 수보다 더 크게 바꿀 수 없는 경우, 바꾸는 값이 현재 값과 가장 큰 차이가 덜나는 값으로 바꿔야댐.
'''

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    number = list(map(int, input()))
    print(number)