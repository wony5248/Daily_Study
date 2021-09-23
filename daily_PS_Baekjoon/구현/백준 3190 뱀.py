from collections import deque
import sys
input = sys.stdin.readline
N = int(input().rstrip())
K = int(input().rstrip())
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
time = 0
start = 2
apple = [[0 for _ in range(N)] for _ in range(N)]
visit = [[0 for _ in range(N)] for _ in range(N)]
cmd = deque()
history = deque()
snake = deque()
for i in range(K):
    x, y = map(int, input().rstrip().split())
    apple[x-1][y-1] = 1
L = int(input())
for i in range(L):
    x, y = input().rstrip().split()
    cmd.append([int(x), y])


def bfs():
    snake.append([0, 0])
    history.append([0, 0])
    global time
    global start
    visit[0][0] = 1
    while snake:
        cx, cy = snake.popleft()
        # print(cx, cy)
        nx = cx + dx[start]
        ny = cy + dy[start]
        if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0:
            history.append([nx, ny])
            snake.append([nx, ny])
            visit[nx][ny] = 1
            time += 1
            if apple[nx][ny] == 0:
                hx, hy = history.popleft()
                visit[hx][hy] = 0
            else:
                apple[nx][ny] = 0

        if cmd:
            ctime, ccmd = cmd.popleft()
            if time == int(ctime):
                if ccmd == "D":
                    start += 1
                    if start == 4:
                        start = 0
                if ccmd == "L":
                    start -= 1
                    if start == -1:
                        start = 3
            else:
                cmd.appendleft([ctime, ccmd])

bfs()
# for i in range(N):
#     print(visit[i])
print(time + 1)
