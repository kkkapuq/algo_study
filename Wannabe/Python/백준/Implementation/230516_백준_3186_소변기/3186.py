import re

K, L, N = map(int, input().split())
record = input()
ans = []
ss = [s.end() - 1 for s in re.finditer('1' * K, record)]
if len(ss) == 0:
    print("NIKAD")
    exit()

for i in range(len(ss) - 1):
    if record[ss[i] + 1:ss[i + 1]].find('0' * L) != -1:
        ans.append(record[ss[i] + 1:ss[i + 1]].find('0' * L) + ss[i] + L + 1)

if record[ss[-1] + 1:].find('0' * L) != -1:
    ans.append(record[ss[-1] + 1:].find('0' * L) + ss[-1] + L + 1)
else:
    ans.append(record.rfind('1') + L + 1)

for s in ans:
    print(s)
