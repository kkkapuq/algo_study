import sys
si = sys.stdin.readline

sets = [' ', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
p, w = map(int, si().strip().split())
word = si().strip()

"""
2 2
DBD CO  O
"""
def same_group(ch1, ch2):
    g = []
    for ch in [ch1, ch2]:
        for i, btn in enumerate(sets):
            try:
                idx = btn.index(ch)
                g.append((i, idx+1))
            except:
                continue

    return g[0][0]==g[1][0], (g[0][1], g[1][1])

def cnter(ch):
    global sets
    for grp in sets:
        if ch in grp:
            return list(grp).index(ch)+1

time, term = 0, 0
prev = word[0]
time = p*cnter(prev)

for i in range(1, len(word)):
    ret, indices = same_group(prev, word[i])
    if prev == ' ' and word[i] == ' ':
        ret = False
    time += w if ret else term
    time += p*cnter(word[i])
    prev = word[i]
print(time)