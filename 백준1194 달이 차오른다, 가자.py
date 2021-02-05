# import sys
# from collections import deque
# s = sys.stdin.readline
# N, M = map(int, s().split())
# dx = [0, -1, 0, 1]
# dy = [-1, 0, 1, 0]
# visit = [[0 for _ in range(M)] for _ in range(M)]
# key = list()
# miro = [[0 for _ in range(M)] for _ in range(M)]
# for i in range(N):
#     miro[i] = s()
# for j in range(N):
#     for k in range(M):
#         if miro[j][k] == 0 and visit[j][k] == 0:
#             visit[j][k] = 1
#             queue = deque()
#             queue.append([j,k])
#             while queue:
#                 x, y = queue.popleft()
#                 for l in range(4):
#                     nx = x + dx[l]
#                     ny = y + dy[l]
#                     if 0<= nx < M and 0<= ny < N and visit[nx][ny] == 0 and miro[nx][ny] = 1:
# print()
# print(miro)
