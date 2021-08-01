from collections import deque
import sys
input = sys.stdin.readline
N,L,R = map(int,input().split())
A = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
zzz = 0
result = 0
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def open(x, y):
    queue = deque()
    global lst
    global isflag
    global isopen
    queue.append([x, y])
    isopen = 1
    visit[x][y] = 1
    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < N and 0 <= ny < N and L <= abs(A[cx][cy] - A[nx][ny]) <= R and visit[nx][ny] == 0:
                isopen += 1
                visit[nx][ny] = 1
                queue.append([nx, ny])
                lst.append([nx, ny])
    if len(lst) > 0:
        isflag = 1


while True:
    isflag = 0
    lst = []
    isopen = 1
    visit = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            human = 0
            if not visit[i][j]:
                open(i, j)
            if isopen > 1:
                lst.append([i, j])
                for ls in lst:
                    human += A[ls[0]][ls[1]]
                for ls in lst:
                    A[ls[0]][ls[1]] = human // len(lst)
                lst = []

    if isflag:
        result += 1
    else:
        break
print(result)