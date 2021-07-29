import sys
input = sys.stdin.readline
from itertools import combinations
N, M = map(int, input().split())
member = [list(map(int, input().split()[1:])) for _ in range(M)]
visit = [i for i in range(M)]
tmp = 0
issolve = 0
result = 0
for i in range(1, N+1):
    tmp += i
for i in range(1, M+1):
    if issolve == 1:
        break
    lst = list(combinations(visit, i))
    for j in lst:  # i명 고른 모든 경우의 수
        se = set()  # i명이 푼문제중 중복 제거
        if issolve == 1:
            break
        for k in j:    # i명중 한명이 풀 수 있는 문제들
            if issolve == 1:
                break
            for l in range(len(member[k])):
                se.add(member[k][l])
            if sum(list(se)) == tmp:
                issolve = 1
                result = i
                break
if issolve == 1:
    print(result)
else:
    print(-1)
