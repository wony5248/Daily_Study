# import sys
# from collections import deque
# final = 0
# result = float("inf")
# dx = [0, -1, 0, 1]
# dy = [-1, 0, 1, 0]
# N, M = map(int, sys.stdin.readline().split())
# lab = []
# flag = [[0 for _ in range(N)] for _ in range(N)]
# chicken_num = 0
# for i in range(N):
#     lab.append(list(map(int, sys.stdin.readline().split())))
# for i in range(N):
#     for j in range(N):
#         if lab[i][j] == 2:
#             chicken_num += 1
#
# def wall(cnum):
#     if cnum == M:
#         bfs()
#         return
#     for l in range(N):
#         for d in range(N):
#             if lab[l][d] == 2 and flag[l][d] == 0 :
#                 lab[l][d] = 0
#                 flag[l][d] = 1
#                 wall(cnum-1)
#                 lab[l][d] = 2
#
#
#
# def bfs():
#     global result
#     global final
#     final += 1
#     print(final)
#     lab1 = [[0 for _ in range(N)] for _ in range(N)]
#     check = [[0 for _ in range(N)] for _ in range(N)]
#     visit = [[0 for _ in range(N)] for _ in range(N)]
#     queue = deque()
#     for i in range(N):
#         for j in range(N):
#             lab1[i][j] = lab[i][j]
#     count = 0
#     for i in range(N):
#         print(lab1[i])
#     print()
#     for i in range(N):
#         for j in range(N):
#             if lab1[i][j] == 2 :
#                 queue.append([i, j])
#     while queue:
#         cx, cy = queue.popleft()
#         visit[cx][cy] = 1
#         for k in range(4):
#             nx = cx + dx[k]
#             ny = cy + dy[k]
#             if 0 <= nx < N and 0 <= ny < N and lab1[nx][ny] == 0 and visit[nx][ny] == 0:
#                 check[nx][ny] = check[cx][cy] + 1
#                 visit[nx][ny] = 1
#                 queue.append([nx, ny])
#             elif 0 <= nx < N and 0 <= ny < N and lab1[nx][ny] == 1 and visit[nx][ny] == 0:
#                 check[nx][ny] = check[cx][cy] + 1
#                 count += check[nx][ny]
#                 visit[nx][ny] = 1
#                 queue.append([nx, ny])
#     result = min(result, count)
#
#
#
#
#
# wall(chicken_num)
# print(result)

from itertools import combinations
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

minV = float('inf')
for ch in combinations(chicken, M):
    sumvV= 0
    for home in house:
        result = []
        for i in ch:
            result.append(abs(home[0] - i[0]) + abs(home[1] - i[1]))
        sumvV += min(result)
        if minV <= sumvV:
            break
    if sumvV < minV:
        minV = sumvV

print(minV)

