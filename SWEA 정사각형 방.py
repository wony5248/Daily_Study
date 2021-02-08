from collections import deque
TC = int(input())
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def bfs(x, y):
    global count
    count = 1
    queue = deque()
    queue.append([x, y])

    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < N and 0 <= ny < N and room[nx][ny] == room[cx][cy] + 1:
                count += 1
                queue.append([nx, ny])
    cntlst.append(count)



for i in range(1, TC+1):
    N = int(input())
    room = [[0 for _ in range(N)] for _ in range(N)]
    result = []
    cntlst = []
    final = []
    for j in range(N):
        room[j] = list(map(int, input().split()))

    for j in range(N):
        for k in range(N):
            if room[j][k] >= 1:
                result.append(room[j][k])
                bfs(j, k)
    for j in range(len(cntlst)):
        if cntlst[j] == max(cntlst):
            final.append(result[j])
    print("#%d %s %d" %(i, final, max(cntlst)))