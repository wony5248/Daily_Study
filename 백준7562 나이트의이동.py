from collections import deque
import sys
T = int(input())
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]
def bfs(startx, starty, destx, desty):
    chess[startx][starty] = 1
    queue = deque()
    queue.append([startx, starty])
    while queue:
        x, y = queue.popleft()
        if x == destx and y == desty:
            print(chess[destx][desty] - 1)
            break
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < length and 0 <= ny < length and chess[nx][ny] == 0:
                queue.append([nx, ny])
                chess[nx][ny] = chess[x][y] + 1
for _ in range(T):
    length = int(input())
    result =0
    chess = [[0 for _ in range(length)] for _ in range(length)]
    startx, starty = list(map(int, input().split()))
    destx, desty = list(map(int, input().split()))
    bfs(startx, starty, destx, desty)

