N = int(input())
chess = [[0 for _ in range(N)] for _ in range(N)]
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
x1, y1, x2, y2 = map(int, input().split())
def bfs():
    chess[x1][y1] = 1
    queue = list()
    cnt = 0
    queue.append([x1, y1])
    while queue:
        cnt += 1
        for i in range(len(queue)):
            x, y = queue.pop(0)
            for j in range(6):
                nx = x + dx[j]
                ny = y + dy[j]
                if nx == x2 and ny == y2:
                    return cnt
                if 0 <= nx < N and 0 <= ny < N and chess[nx][ny] == 0:
                    chess[nx][ny] = 1
                    queue.append([nx, ny])
    return -1

print(bfs())
