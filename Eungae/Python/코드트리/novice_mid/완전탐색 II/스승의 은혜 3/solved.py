import sys
si = sys.stdin.readline

n, b = map(int, si().split())
students = [ list(map(int, si().split())) for _ in range(n)]

answer = 0
for i in students:
    i.append(sum(i[:2]))

students.sort(key=lambda x:x[2])

for i in range(n):
    # 반값 쿠폰 적용 + 배송비
    money = (students[i][0] // 2) + students[i][1]
    # 선물 가능한 학생 수
    temp = 0
    if money > b:
        continue
    else:
        temp += 1
    for j in range(n):
        # 같은 학생 패스
        if i==j:
            continue
        money += students[j][0] + students[j][1]
        if money > b:
            break
        else:
            temp += 1
    
    answer = max(temp, answer)

print(answer)