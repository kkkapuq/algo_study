n = int(input())
nums = list(map(int, input().split()))

if len(nums) == 1:
    print(nums[0])
    exit()

def gcd(a, b):
    while b != 0 :
        a, b = b, a%b
    return a 

answer = nums[0]

for i in range(n-1):
    temp = gcd(answer, nums[i+1])
    answer = answer * nums[i+1] / temp

print(int(answer))