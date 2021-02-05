from collections import deque
miro = [[0 for _ in range(16)] for _ in range(16)]


dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
for i in range(1, 11):
    visit = [[0 for _ in range(16)] for _ in range(16)]
    result = []
    TC = int(input())
    for j in range(16):
        miro[j] = list(map(int, input()))
    queue = deque()
    queue.append([1,1])
    while queue:
        x, y = queue.popleft()
        visit[x][y] = 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 16 and 0 <= ny < 16:
                if miro[nx][ny] == 0 and visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    queue.append([nx, ny])
                if miro[nx][ny] == 3 and visit[nx][ny] == 0:
                    result.append(1)
                    break
    if not result:
        print("#%d 0" %i)
    else:
        print("#%d 1" %i)



