k, n = map(int, input().split())
score = [ list(map(int, input().split())) for _ in range(k)]

answer = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            continue
        
        # i번 개발자가 j번 개발자보다 항상 높은 순위일 때 true
        correct = True

        for lists in score:
            index_i = lists.index(i)
            index_j = lists.index(j)

            if index_i > index_j:
                correct = False
        
        if correct:
            answer += 1

print(answer)