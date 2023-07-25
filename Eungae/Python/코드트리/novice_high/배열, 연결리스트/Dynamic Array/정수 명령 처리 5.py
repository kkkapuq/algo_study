arr = []

n = int(input())
for i in range(n):
    temp = input().split()
    order, num = temp[0], int(temp[1])
    
    if order == 'push_back':
        arr.append(num)
    elif order == 'pop_back':
        arr.pop()
    elif order == 'size':
        print(len(arr))
    else:
        print(arr[num-1])