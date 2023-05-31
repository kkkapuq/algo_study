n = int(input())
com1 = list(map(int, input().split()))
com2 = list(map(int, input().split()))

cnt = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if ( abs(com1[0]-i) <= 2 or abs(com1[0]-i) >= n-2 ) and \
               ( abs(com1[1]-j) <= 2 or abs(com1[1]-j) >= n-2 ) and \
               ( abs(com1[2]-k) <= 2 or abs(com1[2]-k) >= n-2 ):
               cnt += 1
            
            elif ( abs(com2[0]-i) <= 2 or abs(com2[0]-i) >= n-2 ) and \
                 ( abs(com2[1]-j) <= 2 or abs(com2[1]-j) >= n-2 ) and \
                 ( abs(com2[2]-k) <= 2 or abs(com2[2]-k) >= n-2 ):
                 cnt += 1 

print(cnt)