N = int(input())
M = int(input())
connect = [[0 for _ in range(N)] for _ in range(N)]
visit = [0 for _ in range(N)]

for i in range(M):
    x, y = map(int, input().split())
    connect[x-1][y-1] = 1
    connect[y-1][x-1] = 1

def dfs(v):
    visit[v] = 1
    for i in range(N):
        if connect[v][i] == 1 and visit[i] ==0:
            dfs(i)
dfs(0)
cnt =0
for i in range(1, N):
    if visit[i] ==1:
        cnt += 1
print(cnt)


