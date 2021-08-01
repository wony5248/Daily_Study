import sys
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline()) for _ in range(R)]
stack = set(board[0][0])
result = 1

def dfs(x, y, count):
    global result
    if result == 26:
        return
    result = max(result, count)
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in stack:
            stack.add(board[nx][ny])
            dfs(nx, ny, count+1)
            stack.remove(board[nx][ny])



dfs(0, 0, result)

print(result)
