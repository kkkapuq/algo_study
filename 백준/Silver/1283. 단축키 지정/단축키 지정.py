'''
문제 : 단축키 지정
링크 : https://www.acmicpc.net/problem/1283
소요시간 : 
'''
# 대소문자를 구분하지 않으므로, 맵의 형태는 소문자 : 옵션 으로 이루어진다.
# 정답으로 출력할 answer 리스트를 만들고, (단축키, 옵션) 형태로 구성하자.
import sys
se = sys.stdin.readline

n = int(input())
# 단축키를 저장할 맵
shortcut = {}

for _ in range(n):
    words = input().split()

    # 단축키가 할당됐는지 판단하는 flag
    isResistered = False
    
    # 전달받은 단어 단위로 탐색
    for i in range(len(words)):
        temp = words[i].lower()

        # 단어의 첫 글자를 먼저 단축키 등록이 가능한지 확인한다.
        if temp[0] in shortcut:
            continue
        elif temp[0] not in shortcut:
            isResistered = True
            shortcut[temp[0]] = True
            words[i] = '[' + words[i][0] + ']' + words[i][1:]
            print(' '.join(words))
            break

    # 단어 단위를 체크했는데, 단축키가 할당이 되지 않았다면 알파벳 순서로 체크
    if not isResistered:
        for i in range(len(words)):
            temp = words[i].lower()
            for j in range(len(temp)):
                if temp[j] not in shortcut:
                    isResistered = True
                    shortcut[temp[j]] = True
                    words[i] = words[i][:j] + '[' + words[i][j] + ']' + words[i][j+1:]
                    print(' '.join(words))
                    break
            if isResistered:
                break
    
    # 만약 단축키 할당이 안된다면 그냥 단어 자체를 키값으로 넣어버리자.
    if not isResistered:
        print(' '.join(words))