N, M, V = map(int, input().split())
graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
visit = [0 for _ in range(N + 1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1


def dfs(start):
    print(start, end=" ")
    visit[start] = 1
    for i in range(1, N + 1):
        if visit[i] == 0 and graph[start][i] == 1:
            dfs(i)


def bfs(start):
    lst = list()
    lst.append(start)
    visit[start] = 0
    while lst:
        start = lst.pop(0)
        print(start, end=" ")
        for i in range(1, N + 1):
            if visit[i] == 1 and graph[start][i] == 1:
                lst.append(i)
                visit[i] = 0


dfs(V)
print("")
bfs(V)
