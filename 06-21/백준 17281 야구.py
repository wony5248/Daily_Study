import sys
from itertools import permutations
input = sys.stdin.readline


N = int(input())
record = [list(map(int, input().split())) for _ in range(N)]

hitter = [1, 2, 3, 4, 5, 6, 7, 8]       # 1번 선수 제외 나머지 8명의 타자들
answer = 0
for order in permutations(hitter, 8):
    order = list(order)
    order = order[:3] + [0] + order[3:]          # 1번 선수를 4번 타자로
    score = 0
    idx = 0
    for inning in range(N):
        out = 0
        base1 = 0
        base2 = 0
        base3 = 0
        while out < 3:
            if record[inning][order[idx]] == 0:
                out += 1
            elif record[inning][order[idx]] == 1:
                score += base3
                base3 = base2
                base2 = base1
                base1 = 1
            elif record[inning][order[idx]] == 2:
                score += (base2 + base3)
                base3 = base1
                base1 = 0
                base2 = 1
            elif record[inning][order[idx]] == 3:
                score += (base1 + base2 + base3)
                base1 = 0
                base2 = 0
                base3 = 1
            elif record[inning][order[idx]] == 4:
                score += (base1 + base2 + base3 + 1)
                base1 = 0
                base2 = 0
                base3 = 0
            idx += 1
            if idx == 9:
                idx = 0
    answer = max(answer, score)
print(answer)