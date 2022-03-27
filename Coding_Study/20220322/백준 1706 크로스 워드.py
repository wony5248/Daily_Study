import sys
input = sys.stdin.readline

R, C = map(int, input().split())
crossword = [input().rstrip() for _ in range(R)]
visit = [[0 for _ in range(C)] for _ in range(R)]
dx = [0, 1]
dy = [1, 0]

result = []
def solve(x, y, dir, ans):
    cx = x
    cy = y
    cdir = dir
    cans = ans
    nx = cx + dx[dir]
    ny = cy + dy[dir]
    if 0 <= nx < R and 0 <= ny < C and crossword[nx][ny] != "#":
        solve(nx, ny, cdir, cans + crossword[nx][ny])
    else:
        if len(cans) >= 2:
            result.append(cans)
for i in range(R):
    for j in range(C):
        if crossword[i][j] != "#":
            for d in range(2):
                px = i - dx[d]
                py = j - dy[d]
                if 0 <= px < R and 0 <= py < C and crossword[px][py].isalpha():
                    continue
                else:
                    solve(i, j, d, crossword[i][j])
result.sort()
print(result[0])