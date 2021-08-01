import sys
input = sys.stdin.readline
from collections import deque
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
N, M, T = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]
dist = float("inf")



def bfs():
    queue = deque()
    queue.append([0, 0])
    global dist
    visit[0][0] = 1
    while queue:
        x, y = queue.popleft()
        if x == N-1 and y == M-1:
            dist = min(dist, visit[x][y] - 1)
            break
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and castle[nx][ny] == 0 and visit[nx][ny] == 0:
                queue.append([nx, ny])
                visit[nx][ny] = visit[x][y] + 1
            elif 0 <= nx < N and 0 <= ny < M and castle[nx][ny] == 2 and visit[nx][ny] == 0:
                queue.append([nx, ny])
                visit[nx][ny] = visit[x][y] + 1
                dist = abs(visit[nx][ny] - 1 + (N + M - nx - ny - 2))


bfs()
if dist <= T:
    print(dist)
else:
    print("Fail")



# import sys
# input = sys.stdin.readline
# from collections import deque
# dx = [0, -1, 0, 1]
# dy = [-1, 0, 1, 0]
# N, M, T = map(int, input().split())
# castle = [list(map(int, input().split())) for _ in range(N)]
# visit = [[0 for _ in range(M)] for _ in range(N)]
# sword = []
# isflag = 0
# dist = 0
# def bfs():
#     queue = deque()
#     queue.append([0, 0])
#     visit[0][0] = 1
#     while queue:
#         x, y = queue.popleft()
#         for d in range(4):
#             nx = x + dx[d]
#             ny = y + dy[d]
#             if 0 <= nx < N and 0 <= ny < M and castle[nx][ny] == 0 and visit[nx][ny] == 0:
#                 queue.append([nx, ny])
#                 visit[nx][ny] = visit[x][y] + 1
#             elif 0 <= nx < N and 0 <= ny < M and castle[nx][ny] == 2 and visit[nx][ny] == 0:
#                 queue.append([nx, ny])
#                 visit[nx][ny] = visit[x][y] + 1
#                 sword.append([nx, ny])
#
# bfs()
# if not sword and visit[N-1][M-1] == 0:
#     isflag = 1
# elif sword and visit[N-1][M-1] == 0:
#     dist = abs(visit[sword[0][0]][sword[0][1]] - 1 + (N + M - sword[0][0] - sword[0][1] - 2))
# else:
#     dist = min(abs(visit[sword[0][0]][sword[0][1]] - 1 + (N + M - sword[0][0] - sword[0][1] - 2)), visit[N-1][M-1] - 1)
#
# # for i in range(N):
# #     print(visit[i])
# if dist <= T and isflag == 0:
#     print(dist)
# else:
#     print("Fail")
