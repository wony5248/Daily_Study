from collections import deque
dx = [0, -1, 0, 1, 1, -1, -1, 1]
dy = [-1, 0, 1, 0, -1, -1, 1, 1]

while True:
    w, h = map(int, input().split())

    imap = [[0 for _ in range(w)] for _ in range(h)]
    visit = [[0 for _ in range(w)] for _ in range(h)]
    if w == 0 and h == 0:
        break
    for i in range(h):
        island = map(int, input().split())
        imap[i] = list(island)
    count = 0
    for j in range(h):
        for k in range(w):
            if imap[j][k] == 1 and visit[j][k] == 0:
                visit[j][k] = 1
                count += 1
                queue = deque()
                queue.append([j, k])
                while queue:
                    x, y = queue.popleft()
                    for l in range(8):
                        nx = x + dx[l]
                        ny = y + dy[l]
                        if 0 <= nx < h and 0 <= ny < w and imap[nx][ny] == 1 and visit[nx][ny] == 0:
                            visit[nx][ny] = 1
                            queue.append([nx, ny])
            else:
                continue
    print(count)
