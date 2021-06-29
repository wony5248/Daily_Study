import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = list()
count = 0
for i in range(N):
    S.append(input().rstrip())
S = set(S)
for j in range(M):
    x = input().rstrip()
    if x in S:
        count += 1

print(count)