T = int(input())

def dfs(start):
    visit[start] = 1
    for k in range(N):
        if rel[start][k] == 1 and visit[k] == 0:
            dfs(k)


for tc in range(T):
    N, M = map(int, input().split())
    rel = [[0 for _ in range(N)] for _ in range(N)]
    visit = [0 for _ in range(N)]
    count = 0
    for i in range(M):
        x, y = map(int, input().split())
        rel[x-1][y-1] = 1
        rel[y-1][x-1] = 1

    for i in range(N):
        if visit[i] == 0:
            dfs(i)
            count += 1
    print("#%d %d" %(tc+1, count))