import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
dir = {
    0: [-1, 0],    # 북
    1: [0, 1],     # 동
    2: [1, 0],     # 남
    3: [0, -1],    # 서
}
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = 1

def solve(x, y, direction):
    queue = deque()
    global result
    queue.append([x, y, direction]) # 좌표랑 해당 좌표 들어올때의 방향
    area[x][y] = 2
    while queue:
        cx, cy, cdirection = queue.popleft()
        cnt = 0
        for k in range(4):              # 4방면이 막혀있는지 확인하기위해
            nextx = cx + dx[k]
            nexty = cy + dy[k]
            if 0 <= nextx < N and 0 <= nexty < M and area[nextx][nexty] == 0:
                cnt += 1
            # cnt가 0이라면 네면이 청소되었거나 벽인 상태
        if cdirection == 0:     # 왼쪽으로 도는 것을 현재 방향 -1 해줌 0 일땐 3으로 가야하기에
            ndirection = 3
        elif cdirection == 1 or cdirection == 2 or cdirection ==3:
            ndirection = cdirection - 1


        nx = cx + dir[ndirection][0]          # 다음 탐색할곳 - 왼쪽으로 돌았을때
        ny = cy + dir[ndirection][1]
        px = cx - dir[cdirection][0]          # 막혔을때를 가정한 뒤로 한칸 가는거
        py = cy - dir[cdirection][1]
        if 0 <= nx < N and 0 <= ny < M and area[nx][ny] == 0:  # a조건 왼쪽이 청소 안한 곳이라면
            queue.append([nx, ny, ndirection])   # 방향 바꿔주고 한칸 전진
            area[nx][ny] = 2                     # 청소
            result += 1                          # 청소 구역수 + 1
        elif cnt == 0 and 0 <= nx < N and 0 <= ny < M and area[px][py] == 2:
            # c번 조건 네방향 모두 청소 되었거나 벽이고 뒤가 청소구역일때 뒤로 한칸
            queue.append([px, py, cdirection])
        elif cnt == 0 and 0 <= nx < N and 0 <= ny < M and area[px][py] == 1:
            # d 번 조건 네방향 모두 청소 되었거나 벽이고 뒤도 벽인경우 끝
            return
        else: # b번 조건 좌표는 그대로 방향만 바꿔줌
            queue.append([cx, cy, ndirection])


solve(r,c,d)


print(result)

