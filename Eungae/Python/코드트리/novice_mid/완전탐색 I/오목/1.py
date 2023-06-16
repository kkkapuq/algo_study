n = int(input())
nums = [list(input()) for _ in range(n)]
answer = -1

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            maxLen = max(len(nums[i]), len(nums[j]), len(nums[k]))
            # 만약 자릿수가 맞지않다면 가장 큰 자릿수에 맞춰준다.
            if len(nums[i]) < maxLen:
                for _ in range(maxLen - len(nums[i])):
                    nums[i].insert(0, '0')
            if len(nums[j]) < maxLen:
                for _ in range(maxLen - len(nums[j])):
                    nums[j].insert(0, '0')
            if len(nums[k]) < maxLen:
                for _ in range(maxLen - len(nums[k])):
                    nums[k].insert(0, '0')
            # 자릿수별로 더해서 carry가 발생하는지 확인한다.
            flag = True
            for l in range(maxLen):
                if int(nums[i][l]) + int(nums[j][l]) + int(nums[k][l]) > 9:
                    flag = False
                    break
            # 모든 자릿수에서 carry가 발생하지 않는다면 최대값을 갱신해준다.
            if flag:
                answer = max(answer, int(''.join(nums[i])) + int(''.join(nums[j])) + int(''.join(nums[k])))

print(answer)