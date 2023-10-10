n = int(input())
# basic idea -> [[1, 1, 0],
#                [1, 0, 0],
#                [0, 1, 0]]을 n-2번 거듭제곱하고 [F0; F1; F2]에 곱하면 된다?
# F0 = 0, F1 = 1, F2 = 1
def multiply(x, y):
    result = [[0]*len(y[0]) for _ in range(2)]
    for i in range(2):
        for c in range(len(y[0])):
            total = 0
            for j in range(2):
                total += x[i][j]*y[j][c]
            result[i][c] = total%LARGE
    return result


def pow(mat, k): #여기가 문제
    if k == 1:
        return mat
    elif k%2 == 1:
        return multiply(pow(mat, k-1), mat)
    else:
        return pow(multiply(mat, mat), k//2)

if __name__ == "__main__":
    LARGE = 1000000007
    factor = [[1, 1], [1, 0]]
    init = [[1], [1]]
    if n > 2:
        pwr = pow(factor, n-2)
        for i in range(2):
            print(*pwr[i])
        answer = multiply(pwr, init)[0][0]
        print(answer)
    else:
        print(init[1-n][0])