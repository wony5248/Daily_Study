import sys
input = sys.stdin.readline
omok = [list(map(int, input().split())) for _ in range(19)]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
result = []


def solve(cnt, x, y, dir, col):
    cx = x
    cy = y
    cdir = dir
    ccol = col
    ccnt = cnt
    nx = cx + dx[dir]
    ny = cy + dy[dir]
    if ccnt == 5:
        if 0 <= nx < 19 and 0 <= ny < 19 and omok[nx][ny] != ccol:
            result.append([ccol, cx+1, cy+1])
            return
        if nx < 0 or nx >= 19 or ny < 0 or ny >= 19:
            result.append([ccol, cx + 1, cy + 1])
            return
        if 0 <= nx < 19 and 0 <= ny < 19 and omok[nx][ny] == ccol:
            return

    if 0 <= nx < 19 and 0 <= ny < 19 and omok[nx][ny] == ccol:
        solve(ccnt+1, nx, ny, cdir, ccol)


for i in range(19):
    for j in range(19):
        if omok[i][j] == 1:
            for d in range(8):
                nx = i + dx[d]
                ny = j + dy[d]
                px = i - dx[d]
                py = j - dy[d]
                if 0 <= nx < 19 and 0 <= ny < 19 and omok[nx][ny] == 1:
                    if 0 > px or 19 <= px or 0 > py or 19 <= py or (0 <= px < 19 and 0 <= py < 19 and omok[px][py] != 1):
                        solve(1, i, j, d, 1)
        elif omok[i][j] == 2:
            for d in range(8):
                nx = i + dx[d]
                ny = j + dy[d]
                px = i - dx[d]
                py = j - dy[d]
                if 0 <= nx < 19 and 0 <= ny < 19 and omok[nx][ny] == 2:
                    if 0 > px or 19 <= px or 0 > py or 19 <= py or (
                            0 <= px < 19 and 0 <= py < 19 and omok[px][py] != 2):
                        solve(1, i, j, d, 2)

result.sort(key=lambda x: (x[2], x[1]))

if result:
    print(result[0][0])
    print(result[0][1], result[0][2])
else:
    print(0)