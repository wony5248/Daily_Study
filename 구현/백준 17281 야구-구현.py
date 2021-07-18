import sys
from itertools import permutations
input = sys.stdin.readline


N = int(input())
record = [list(map(int, input().split())) for _ in range(N)]

hitter = [1, 2, 3, 4, 5, 6, 7, 8]
answer = 0
for i in permutations(hitter, 8):
    i = list(i)
    i = i[:3] + [0] + i[3:]
    score = 0
    idx = 0
    for j in range(N):
        out = 0
        base1, base2, base3 = 0, 0, 0
        while out < 3:
            if record[j - 1][i[idx]] == 0:
                out += 1
            elif record[j - 1][i[idx]] == 1:
                score += base3
                base1, base2, base3 = 1, base1, base2
            elif record[j - 1][i[idx]] == 2:
                score += (base2 + base3)
                base1, base2, base3 = 0, 1, base1
            elif record[j - 1][i[idx]] == 3:
                score += (base1 + base2 + base3)
                base1, base2, base3 = 0, 0, 1
            elif record[j - 1][i[idx]] == 4:
                score += (base1 + base2 + base3 + 1)
                base1, base2, base3 = 0, 0, 0
            idx += 1
            if idx == 9:
                idx = 0
    answer = max(answer, score)
print(answer)