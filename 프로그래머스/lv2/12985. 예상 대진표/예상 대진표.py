def isFight(a, b):
    # 둘중 큰 수가 짝수고, 차이가 1인 경우
    if (a > b and a % 2 == 0 and a-b == 1) or \
        (a < b and b % 2 == 0 and b-a == 1):
        return True
    return False

def solution(n,a,b):
    answer = 1
    while True:
        if isFight(a, b):
            break
        else:
            # 현재 라운드에서 싸우는게 아니라면, 다음 라운드를 위해 번호를 갱신해준다.
            a = (a+1) // 2
            b = (b+1) // 2
            answer += 1

    return answer