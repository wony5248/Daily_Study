from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
check = [[100 for _ in range(N+1)] for _ in range(N+1)]
result = 0
minV = 10001
for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1


def bfs(x, step, start):
    queue = deque()
    visit[start][start] = 1
    check[start][start] = 0
    queue.append([x, step, start])
    while queue:
        cx, cstep, cstart = queue.popleft()
        for j in range(1, N+1):
            if graph[cx][j] and not visit[cx][j]:      # 연결되어 있고 방문 안했으면
                visit[cx][j] = 1
                if cstep + 1 < check[start][j]:      # 지금 까지 거쳐온 친구수가 원래 저장되어있던 수보다 작으면
                    check[start][j] = cstep + 1      # 바꿔줌
                queue.append([j, cstep+1, cstart])


for i in range(1, N+1):
    visit = [[0 for _ in range(N+1)] for _ in range(N+1)]
    bfs(i, 0, i)


for i in range(1, N+1):
    if sum(check[i][1:]) < minV:
        minV = sum(check[i][1:])
        result = i

print(result)



# import sys
# input = sys.stdin.readline
# INF = float("INF")
# N, M = map(int, input().split())
# graph = [[INF for _ in range(N+1)] for _ in range(N+1)]
#
# for i in range(M):
#     x, y = map(int, input().split())
#     graph[x][y] = 1
#     graph[y][x] = 1
#
# for k in range(1, N+1):
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             if i == j:
#                 graph[i][j] = 0
#             else:
#                 graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
#
# result = []
# for i in range(1, N+1):
#     result.append(sum(graph[i][1:]))
#
# print(result.index(min(result)) + 1)
#
