import sys
from collections import deque
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
answer = 0
arr = [list(input()) for _ in range(12)]


def bfs(x, y, chain):

    queue = deque()
    queue.append([x, y])
    chained.append([x, y])
    visit[x][y] = 1
    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < 12 and 0 <= ny < 6 and visit[nx][ny] == 0 and arr[nx][ny] == chain:
                visit[nx][ny] = 1
                queue.append([nx, ny])
                chained.append([nx, ny])


def gravity():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if arr[j][i] != "." and arr[k][i] == ".":
                    arr[k][i] = arr[j][i]
                    arr[j][i] = "."
                    break


while True:
    ischain = False
    visit = [[0 for _ in range(6)] for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if arr[i][j] != "." and visit[i][j] == 0:
                chained = []
                bfs(i, j, arr[i][j])
                if len(chained) > 3:
                    ischain = True
                    for k in chained:
                        arr[k[0]][k[1]] = "."
    # for i in range(12):
    #     print(arr[i])
    # print()
    if ischain is False:
        break
    gravity()
    # for i in range(12):
    #     print(arr[i])
    # print()
    answer += 1
print(answer)