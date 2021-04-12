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
            if paper[x][y] != paper[i][j]:           # 하나라도 색이 다르다면 4등분 해줌
                                                     # 4등분후 각각의 사분면에 대해서 재귀로 탐색
                solve(x, y, size // 2)             # 1사분면
                solve(x, y+size // 2, size // 2)      # 2사분면
                solve(x + size // 2, y, size // 2)    # 3사분면
                solve(x + size // 2, y + size // 2, size // 2)     # 4사분면
                return

    if paper[x][y] == 0:           # 여기 까지 왔으면 구역내 모든 종이가 색이 같은거   -> 탐색 시작 지점이 0이면 흰색 +1
        iswhite += 1
        return
    else:
        isblue += 1
        return

solve(0, 0, N)
print(iswhite)
print(isblue)
