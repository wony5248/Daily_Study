import sys
from collections import deque
import copy
result = 250
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
N, M = map(int, sys.stdin.readline().split())
visit = [[0 for _ in range(N)] for _ in range(N)]
lab = []
queue = deque()
for i in range(N):
    lab.append(list(map(int, sys.stdin.readline().split())))


def active(activenum, queue):
    if activenum == M:
        print("end")
        return bfs(queue)

    for i in range(N):
        for j in range(N):
            if lab[i][j] == 2:
                lab[i][j] = 1
                queue.append([i, j])
                x = active(activenum+1, queue)
                queue = copy.deepcopy(x)
                if queue:
                    queue.pop()
                lab[i][j] = 0


def bfs(queue):
    global result
    global visit
    queue1 = deque()
    queue1 = copy.deepcopy(queue)
    visit = [[0 for _ in range(N)] for _ in range(N)]
    count = 0
    isflag = False
    while queue:
        print(queue)
        cx, cy = queue.popleft()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0 and lab[nx][ny] != 1:
                queue.append([nx, ny])
                visit[nx][ny] = visit[cx][cy] + 1
    for i in range(N):
        for j in range(N):
            if lab[i][j] == 0:
                isflag = True
            count = max(count, lab[i][j])
    if isflag != True:
        result = min(result, count)
    print(queue1)
    return queue1


active(0, queue)

if result == 250:
    print(-1)
else:
    print(result)
