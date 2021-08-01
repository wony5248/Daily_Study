from collections import deque
T = int(input())

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


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
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]
    visit = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if table[j][k] > 0 and visit[j][k] == 0:
                bfs(j,k)
                result.append([stack[1][0] - stack[0][0] + 1, stack[1][1] - stack[0][1] + 1])
    print("#%d" % (i+1), end=" ")
    # print(len(result), end=" ")
    result.sort(key= lambda x : (x[0] * x[1], x[0]))
    for j in range(len(result)):
        for k in range(len(result[j])):
            print(result[j][k], end=" ")
    print()

