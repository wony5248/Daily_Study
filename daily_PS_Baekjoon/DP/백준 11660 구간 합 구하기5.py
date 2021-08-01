import sys
N, M = map(int, sys.stdin.readline().split())
lst = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(N):
    lst[i] = list(map(int, sys.stdin.readline().split()))




copylst = [[0 for _ in range(N + 1)] for _ in range(N+1)]
for k in range(2):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if k == 0:
                copylst[i][j] = copylst[i][j - 1] + lst[i - 1][j - 1]
            else:
                copylst[i][j] += copylst[i-1][j]

for i in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    if x1 == 1 and y1 == 1:
        print(copylst[x2][y2])
    elif x1 == 1 :
        print(copylst[x2][y2] - copylst[x2][y1-1])
    elif y1 == 1:
        print(copylst[x2][y2] - copylst[x1-1][y2])
    else:
        print(copylst[x2][y2] - copylst[x1-1][y2] - copylst[x2][y1-1] + copylst[x1-1][y1-1])



# import sys
# N, M = map(int, sys.stdin.readline().split())
# lst = [[0 for _ in range(N+1)] for _ in range(N+1)]
#
# for i in range(N):
#     lst[i] = list(map(int, sys.stdin.readline().split()))
#
# copylst = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
# for i in range(1, N + 1):
#     for j in range(1, N+1):
#         copylst[i][j] = copylst[i][j - 1] + lst[i - 1][j - 1]
#
# for i in range(M):
#     result = 0
#     x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
#     for j in range(x1, x2+1):
#         result += (copylst[j][y2] - copylst[j][y1-1])
#     print(result)
