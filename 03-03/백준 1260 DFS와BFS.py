from collections import deque
N, M, V = map(int, input().split())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visit = [0 for _ in range(N+1)]
visit1 = [0 for _ in range(N+1)]
def dfs(start):           # 처음 노드에 연결된 첫노드 탐색 -> 그 노드에 연결된 첫 노드 탐색 ...->
    print(start, end=" ")    #탐색한 값 출력
    visit[start] = 1
    for i in range(N+1):     #
        if graph[start][i] == 1 and visit[i] == 0:    # 연결된 애중에 먼저 나오고 방문 안했으면
            dfs(i)                                    # 재귀  탐색



def bfs(start):                      # 처음 탐색 한 노드에서 탐색할수 있는 친구 다 queue에 넣음 -> 탐색 -> 첫 노드에 연결된 애들 먼저 탐색
    queue = deque()
    queue.append(start)
    visit1[start] = 1
    while queue:
        x = queue.popleft()
        print(x, end=" ")
        for i in range(N+1):
            if graph[x][i] == 1 and visit1[i] == 0:
                visit1[i] = 1
                queue.append(i)


for i in range(M):
    x, y = map(int, input().split())     # x 와 y는 연결되어 있음
    graph[x][y] = 1
    graph[y][x] = 1



dfs(V)
print()
bfs(V)