n = int(input())
strs = input()

answer = 999999

for i in range(n):
    # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    cnt = 1
    sentence = strs[i]
    # 현재 인덱스 기준으로 연속 부분 문자열을 찾는다
    for j in range(i+1, n):
        wordToAscii = ord(strs[j])
        if ord(strs[j-1]) + 1 == ord(strs[j]):
            cnt += 1
            strs += strs[j]
        else:
            break
    if strs.count(sentence) < 2:
        answer = min(answer, cnt)
print(answer)