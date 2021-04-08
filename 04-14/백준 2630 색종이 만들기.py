import sys
input = sys.stdin.readline
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

iswhite = 0
isblue = 0

def solve(x, y, size):
    global iswhite, isblue
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[x][y] != paper[i][j]:
                solve(x, y, size // 2)
                solve(x, y+size // 2, size // 2)
                solve(x + size // 2, y, size // 2)
                solve(x + size // 2, y + size // 2, size // 2)
                return

    if paper[x][y] == 0:
        iswhite += 1
        return
    else:
        isblue += 1
        return

solve(0, 0, N)
print(iswhite)
print(isblue)
