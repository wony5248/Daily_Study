from collections import deque
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

T = int(input())


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    while queue:
        cx, cy = queue.popleft()
        for j in range(4):
            nx = cx + dx[j]
            ny = cy + dy[j]
            if 0 <= nx < size and 0 <= ny < size:
                if distance[nx][ny] > distance[cx][cy] + graph[nx][ny]:
                    distance[nx][ny] = distance[cx][cy] + graph[nx][ny]
                    queue.append([nx, ny])




for i in range(T):
    size = int(input())
    graph = [list(map(int, input())) for _ in range(size)]
    distance = [[9999 for _ in range(size)] for _ in range(size)]
    distance[0][0] = 0
    bfs(0, 0)
    print("#%d %d" %(i+1, distance[size-1][size-1]))

print(graph)