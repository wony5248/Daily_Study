import sys
from collections import deque
from itertools import combinations
result = 10000
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
N, M = map(int, sys.stdin.readline().split())
lab = []
lst = []


def bfs():
    global result
    global visit
    count, count2 = 0, 0

    while queue:
        qlen = len(queue)
        isflag, isflag2 = 0, 1
        for idx in range(qlen):
            cx, cy = queue.popleft()
            for k in range(4):
                nx = cx + dx[k]
                ny = cy + dy[k]
                if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0 and lab[nx][ny] != 1:
                    queue.append([nx, ny])
                    visit[nx][ny] = 1
                    isflag = 1
                    if lab[nx][ny] == 0:
                        isflag2 = 0
        if isflag == 1:
            if isflag2 == 0:
                if count2:
                    count += count2 + 1
                    count2 = 0
                else:
                    count += 1
            else:
                count2 += 1
    for j in range(N):
        for k in range(N):
            if lab[j][k] != 1 and visit[j][k] == 0:
                return 10000
    return count



for i in range(N):
    lab.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            lst.append([i, j])
queue1 = list(combinations(lst, M))

for i in queue1:
    queue = deque()
    visit = [[0 for _ in range(N)] for _ in range(N)]
    for j in i:
        x, y = j
        visit[x][y] = 1
        queue.append(j)
    result = min(result, bfs())


if result == 10000:
    print(-1)
else:
    print(result)

