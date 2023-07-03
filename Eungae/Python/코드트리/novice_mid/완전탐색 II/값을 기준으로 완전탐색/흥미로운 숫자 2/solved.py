answer = 0

x, y = map(int, input().split())

for i in range(x, y+1):
    # dict로 만들어서 문자별로 몇개있는지 확인한 다음에
    # value만 따져서 1개 count가 1개 있는 경우만 answer += 1
    dic = {}
    for j in str(i):
        if j not in dic:
            dic[j] = 1
        else:
            dic[j] += 1
        
    cntList = list(dic.values())
    if len(cntList) == 2 and cntList.count(1) == 1:
        answer += 1

print(answer)