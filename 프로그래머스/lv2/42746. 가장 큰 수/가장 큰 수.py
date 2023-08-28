def solution(numbers):
    arr = [str(i) for i in numbers]
    arr.sort(key=lambda x:x*3, reverse=True)

    return str(int(''.join(arr)))