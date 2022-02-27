import sys
input = sys.stdin.readline

N = int(input().rstrip())

friends = [list(input().rstrip()) for _ in range(N)]
visit = [[0 for _ in range(N)] for _ in range(N)]
result = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if friends[i][j] == 'Y' or (friends[i][k] == 'Y' and friends[k][j] == 'Y'):
                visit[i][j] = 1

for d in visit:
    result = max(result, sum(d))


print(result)