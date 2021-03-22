# import sys
#
# T = int(sys.stdin.readline())
#
#
# def dfs(start):
#     visit[start] = 1
#     global count
#     count += 1
#     for i in range(N):
#         if visit[i] == 0 and nation[start][i] == 1:
#             dfs(i)
#
#
#
# for _ in range(T):
#     N, M = map(int, sys.stdin.readline().split())
#     nation = [[0 for _ in range(N)] for _ in range(N)]
#     visit = [0 for _ in range(N)]
#     count = 0
#     for i in range(M):
#         x, y = map(int, sys.stdin.readline().split())
#         nation[x-1][y-1] = 1
#         nation[y-1][x-1] = 1
#     dfs(0)
#     print(count-1)


import sys                  # 모두 연결되어있고 각 간선이 비행기 종류 이므로 spanning tree 의 간선의수 가 답

T = int(sys.stdin.readline())


for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    count = 0
    for i in range(M):
        x, y = map(int, sys.stdin.readline().split())

    print(N-1)