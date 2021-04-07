from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
size = 2
eat = 0
result = 0
def bfs(x, y):
    global feed
    feed = []           # 먹을수 있는애들 넣을 배열   ([먹이의 y좌표, 먹이의 x좌표, 먹이까지의 거리])
    global size          # 아기상어의 크기
    visit = [[0 for _ in range(N)] for _ in range(N)]
    check = [[0 for _ in range(N)] for _ in range(N)]       # 이동한 거리 저장 배열
    queue = deque()
    queue.append([x, y])
    visit[x][y] = 1
    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0 and space[nx][ny] <= size:   # 방문 안했고 지나갈 수 있는 곳일때
                queue.append([nx, ny])               # 방문
                visit[nx][ny] = 1
                check[nx][ny] = check[cx][cy] + 1
                if 0 < space[nx][ny] < size:                  # 먹을수 있는 곳일때
                    feed.append([nx, ny, check[nx][ny]])     # 먹을 후보군에 넣어줌


for i in range(N):
    for j in range(N):
        if space[i][j] == 9:           # 맨처음 아기상어 위치에서 bfs 시작 그뒤 아기상어 원래 위치는 0으로 초기화
            bfs(i, j)
            space[i][j] = 0

while feed:         # 아기 상어가 먹을 수 있는 애들이 있을때
    feed.sort(key= lambda x: (x[2], x[0], x[1]))      # 가장 가까운 먹이 먹으러 감
    rx, ry, dist = feed[0][0], feed[0][1], feed[0][2]
    space[rx][ry] = 0                           # 먹이 위치 0으로 초기화
    result += dist                              # result 에  이동한 거리 추가
    eat += 1                                    # 현재 크기에서 먹은 횟수 +1
    if eat == size:                             # 먹은 횟수가 size랑 같으면
        size += 1                               # size +1 and 먹은 횟수 0으로 초기화
        eat = 0
    bfs(rx, ry)

print(result)




