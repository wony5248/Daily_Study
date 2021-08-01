from collections import deque
T = int(input())

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def solve(p1, p2):
    if dp[p1][p2] != -1:
        return dp[p1][p2]
    else:
        minV = float("inf")
        for j in range(p1, p2, 1):
            minV = min(minV, solve(p1, j) + solve(j + 1, p2) + final[p1][0] * final[j][1] * final[p2][1] )
        dp[p1][p2] = minV
        return dp[p1][p2]


def bfs(x, y):
    queue = deque()
    queue.append([x,y])
    global stack
    stack = []
    stack.append([x, y])
    stack.append([x, y])
    visit[x][y] = 1
    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < n and 0 <= ny < n and table[nx][ny] > 0 and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                queue.append([nx, ny])
                stack.pop()
                stack.append([nx, ny])


for i in range(T):
    result = []
    final = []
    dp = [[-1 for _ in range(30)] for _ in range(30)]
    answer = 0
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]
    visit = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if table[j][k] > 0 and visit[j][k] == 0:
                bfs(j,k)
                result.append([stack[1][0] - stack[0][0] + 1, stack[1][1] - stack[0][1] + 1])
    final.append(result.pop(0))

    loc = 0
    while result:
        if result[loc][1] == final[0][0] and result[loc][0] == final[len(final) - 1][1]:
            if result[loc][0] < result[loc][1]:
                final.insert(0, result.pop(loc))
                loc = 0
            else:
                final.append(result.pop(loc))
                loc = 0
        elif result[loc][1] == final[0][0]:
            final.insert(0, result.pop(loc))
            loc = 0
        elif result[loc][0] == final[len(final) - 1][1]:
            final.append(result.pop(loc))
            loc = 0
        else:
            loc += 1

    for j in range(len(final)):
        for k in range(len(final)):
            if j == k:
                dp[j][k] = 0
    solve(0, len(final) - 1)
    print("#%d %d" % (i + 1, dp[0][len(final) - 1]))






