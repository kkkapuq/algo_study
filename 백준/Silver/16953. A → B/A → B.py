'''
문제 : A->B
링크 : https://www.acmicpc.net/problem/16953
소요시간 : 17:00
'''
# 인덱스 에러나서 int로 변경
a, b = map(int, input().split())
cnt = 1

# b부터 뒤에 1이 있으면 1을 뒤에서빼주고, 2로 나눠준다.
while a != b:
    temp = b
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    cnt += 1

    if temp == b:
        cnt = -1
        break
print(cnt)