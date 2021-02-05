from collections import deque
dx = []
dy = []


for _ in range(10):
    TC = int(input())
    sadari = [[0 for _ in range(101)] for _ in range(100)]
    visit = [[0 for _ in range(100)] for _ in range(100)]
    queue = deque()
    for i in range(100):
        sadari[i] = list(map(int, input().split()))
    for j in range(100):
        if sadari[99][j] == 2:
            queue.append([99, j])
            while queue:
                x, y = queue.popleft()
                visit[x][y] = 1

                if x == 0:
                    queue.append([x, y])
                    print("#%d %d" % (TC, y))
                    break
                elif y > 0 and sadari[x][y - 1] == 1 and visit[x][y - 1] == 0:
                    nx = x
                    ny = y - 1
                    queue.append([nx, ny])
                elif y < 99 and sadari[x][y + 1] == 1 and visit[x][y + 1] == 0:
                    nx = x
                    ny = y + 1
                    queue.append([nx, ny])
                else:
                    nx = x - 1
                    ny = y
                    queue.append([nx, ny])
    dx, dy = queue.popleft()


