from collections import deque

T = int(input())
tunnel = {
    0: (),
    1: ((0, -1), (-1, 0), (0, 1), (1, 0)),
    2: ((-1, 0), (1, 0)),
    3: ((0, -1), (0, 1)),
    4: ((-1, 0), (0, 1)),
    5: ((0, 1), (1, 0)),
    6: ((0, -1), (1, 0)),
    7: ((0, -1), (-1, 0))
}


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    while queue:
        cx, cy = queue.popleft()
        global count
        for dx, dy in tunnel[location[cx][cy]]:
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < N and 0 <= ny < M:
                if (-dx, -dy) in tunnel[location[nx][ny]] and visit[nx][ny] == 0 and location[nx][ny]:
                    visit[nx][ny] = visit[cx][cy] + 1
                    queue.append([nx, ny])
                    if visit[nx][ny] <= L:
                        count += 1


for tc in range(T):
    N, M, R, C, L = map(int, input().split())
    location = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0 for _ in range(M)] for _ in range(N)]
    count = 1
    visit[R][C] = 1
    bfs(R, C)
    print("#%d %d" %(tc+1, count))