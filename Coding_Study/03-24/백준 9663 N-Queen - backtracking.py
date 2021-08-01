
N = int(input())
sero = [0 for _ in range(N)]                    # 세로
leftup = [0 for _ in range(N*2 - 1)]             # 왼쪽 아래에서 오른쪽 위로 가는 대각선 /
rightdown = [0 for _ in range(N*2 - 1)]          # 왼쪽 위에서 오른쪽 아래로 가는 대각선 /
result = 0

def dfs(x):       # x = 행  y = 열
    global result
    if x == N:                               # 퀸을 N개 놓았다면 result +1 해주고 return
        result += 1
        return
    for y in range(N):                           # 가로로 이동하면서
       if sero[y] == 0 and leftup[x + y] == 0 and rightdown[x-y + N - 1] == 0:  # 세로와 양쪽 대각선이 모두 0이면
           sero[y] = leftup[x + y] = rightdown[x - y + N - 1] = 1
           dfs(x + 1)
           sero[y] = leftup[x + y] = rightdown[x - y + N - 1] = 0

dfs(0)
print(result)

