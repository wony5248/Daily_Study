N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
check = [[0 for _ in range(N)] for _ in range(N)]


def dfs(x, y):        #  x = 탐색할경로 y 탐색 시작했던 곳
    for i in range(N):
        if graph[x][i] and not visit[i]:      # 연결되어 있고 방문 안했으면
            visit[i] = 1
            check[y][i] = 1        # 갈 수 있는 곳  y -> i
            dfs(i, y)



for i in range(N):
    visit = [0 for _ in range(N)]
    dfs(i, i)


for i in range(N):
    for j in range(N):
        print(check[i][j], end=" ")
    print()