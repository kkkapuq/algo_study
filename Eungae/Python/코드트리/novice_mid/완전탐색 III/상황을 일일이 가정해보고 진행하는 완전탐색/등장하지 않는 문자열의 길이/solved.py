n = int(input())
strs = input()

answer = 999999

# 길이가 i+1 짜리 부분 문자열은 얼마나 나오는지 저장하는 공간
length = [0] * (n+1)


for i in range(n):
    sentence = strs[i]
    length[0] += 1
    
    # 현재 인덱스 기준으로 연속 부분 문자열을 찾는다
    for j in range(i+1, n):
        sentence += strs[j]
        if strs.count(sentence) >= 2:
            length[len(sentence)-1] += 1
            continue
        else:
            break

for i in range(len(length)):
    if length[i] == 0:
        answer = i+1
        break

print(answer)