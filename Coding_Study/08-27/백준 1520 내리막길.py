import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
from collections import deque
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
M, N = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(M)]
check = [[-1 for _ in range(N)] for _ in range(M)]
arr = set()
def dfs(cx, cy):
    if cx == M-1 and cy == N-1:
        return 1
    if check[cx][cy] == -1:
        check[cx][cy] = 0
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < M and 0 <= ny < N and jido[cx][cy] > jido[nx][ny]:
                cnt = dfs(nx, ny)
                check[cx][cy] += cnt
    return check[cx][cy]

print(dfs(0, 0))
