import sys
input = sys.stdin.readline

N = int(input())
animal = list(map(int, input().split()))
total = [0] * 41
ex_total = 2

for a in animal:
    total[a] += 1

tmp = True
for cnt in total: #조건탐색
    if cnt > ex_total:
        tmp = False
        break
    ex_total = cnt

if tmp:
    print(2 ** (total.count(2) + (1 if 1 in total else 0)))
else:
    print(0)