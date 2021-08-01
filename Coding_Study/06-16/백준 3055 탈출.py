from collections import deque
import sys
R, C = map(int, input().split())
tmap = [list(input()) for _ in range(R)]
check = [[0 for _ in range(C)] for _ in range(R)]
visit = [[0 for _ in range(C)] for _ in range(R)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
isflag = 0


def bfs():
    cx, cy = queue.popleft()
    visit[cx][cy] = 1
    global isflag
    while queue:
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < R and 0 <= ny < C and tmap[nx][ny] == "." and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                tmap[nx][ny] = "S"
                check[nx][ny] = check[cx][cy] + 1
            elif 0 <= nx < R and 0 <= ny < C and tmap[nx][ny] == "D":
                check[nx][ny] = check[cx][cy] + 1
                isflag = 1


def water():
    while queue1:
        cx, cy = queue1.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < R and 0 <= ny < C and tmap[nx][ny] == ".":
                tmap[nx][ny] = "*"


while True:
    queue1 = deque()
    queue = deque()
    result = deque()
    for i in range(R):
        for j in range(C):
            if tmap[i][j] == "*":
                queue1.append([i, j])
            elif tmap[i][j] == "D":
                result.append([i, j])
            elif tmap[i][j] == "S":
                print(i, j)
                tmap[i][j] = "."
                queue.append([i, j])
    for i in range(R):
        print(tmap[i])
    print()

    if isflag == 1:
        rx, ry = result.popleft()
        print(check[rx][ry])
        break
    elif isflag == 0 and not queue:
        print("KAKTUS")
        break
    water()
    bfs()

