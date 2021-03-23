import sys
input = sys.stdin.readline
R, C, T = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(R)]
cgrid = [[0 for _ in range(C)] for _ in range(R)]
air = []
result = 0
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
for i in range(R):
    for j in range(C):
        if grid[i][j] == -1:
            air.append([i,j])
        cgrid[i][j] = grid[i][j]


def clean():         # 공기청정기 돌리는 함수
    hx, hy = air[0]           # 위 -1의 좌표
    lx, ly = air[1]
    for i in range(hx-1, 0, -1):          # 위 공기청정기 ↓ 방향
        cgrid[i][0] = cgrid[i-1][0] 
    for i in range(C-1):                 #  위 공기 청정기 <- 방향
        cgrid[0][i] = cgrid[0][i+1]
    for i in range(hx):                 # 위 공기 청정기 ↑ 방향
        cgrid[i][C-1] = cgrid[i+1][C-1]
    for i in range(C-1, 0, -1):           # 위 공기 청정기 -> 방향
        cgrid[hx][i] = cgrid[hx][i-1]

    for i in range(lx+1, R-1):             # 아래 공기청정기 ↑ 방향
        cgrid[i][0] = cgrid[i+1][0]   
    for i in range(C-1):                  # 아래 공기청정리 <- 방향
        cgrid[R-1][i] = cgrid[R-1][i+1]
    for i in range(R-1, lx, -1):            # 아래 공기 청정기 ↓ 방향
        cgrid[i][C-1] = cgrid[i-1][C-1]
    for i in range(C-1, 0, -1):          # 아래 공기청정기 -> 방향
        cgrid[lx][i] = cgrid[lx][i-1]
    cgrid[hx][1] = 0
    cgrid[lx][1] = 0

    for i in range(R):
        for j in range(C):
            grid[i][j] = cgrid[i][j]
def solve():            # 미세먼지 퍼지는 함수
    for i in range(R):
        for j in range(C):
            isdir = 0            #  해당 좌표가 몇군데로 퍼질수 있는지 확인하는 변수

            if grid[i][j] > 0:            # 해당 좌표가 미세 먼지라면
                if i < R-1 and grid[i+1][j] != -1:        # 아래쪽이 공기 청정기가 아니고 전체 범위 내라면
                    cgrid[i+1][j] += grid[i][j] // 5      # 아래쪽에 미세먼지 1//5 나눠줌
                    isdir += 1                            # 퍼질수 있는곳 1 추가
                if i > 0 and grid[i-1][j] != -1:          # 위쪽
                    cgrid[i-1][j] += grid[i][j] // 5
                    isdir += 1
                if j < C-1 and grid[i][j+1] != -1:        # 오른쪽
                    cgrid[i][j+1] += grid[i][j] // 5
                    isdir += 1
                if j > 0 and grid[i][j-1] != -1:         # 왼쪽
                    cgrid[i][j-1] += grid[i][j] // 5
                    isdir += 1
            cgrid[i][j] -= (grid[i][j] // 5) *isdir       # 퍼진수 * 먼지수//5 를 빼줌



while T:
    T -= 1
    solve()
    clean()

for i in range(R):
    for j in range(C):
        if cgrid[i][j] > 0:
            result += cgrid[i][j]

print(result)




