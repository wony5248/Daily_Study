from collections import deque

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
graph = [[0 for _ in range(5)] for _ in range(5)]

result = set()
def bfs(x, y, num):
    queue = deque()
    queue.append([x, y, num])
    while queue:
        cx, cy, cnum = queue.popleft()
        for l in range(4):
            nx = cx + dx[l]
            ny = cy + dy[l]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if len(cnum) == 6:
                    result.add(cnum)
                else:
                    queue.append([nx, ny, cnum+graph[nx][ny]])




for j in range(5):
    graph[j] = list(input().split())
for j in range(5):
    for k in range(5):
        bfs(j, k, graph[j][k])
print(len(result))
