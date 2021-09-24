import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]
maxV = -100000000
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
def dfs(x, y, cnt, sumV):
    global maxV
    if cnt == K:
        maxV = max(maxV, sumV)
        return
    for i in range(x, N):
        for j in range(M):
            istrue = 1
            if visit[i][j]:
                continue
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < N and 0 <= ny < M and visit[nx][ny]:
                    istrue = 0
            if istrue:
                visit[i][j] = 1
                dfs(i, j, cnt + 1, sumV + pan[i][j])
                visit[i][j] = 0








dfs(0, 0, 0, 0)
print(maxV)