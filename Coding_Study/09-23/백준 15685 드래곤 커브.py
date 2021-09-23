# from collections import deque
# N = int(input())
# curve = [[0 for _ in range(101)] for _ in range(101)]
# dx = [0, -1, 0, 1]
# dy = [1, 0, -1, 0]
# 0
# 1
# 2 1
# 2 3 2 1
# 2 3 0 3 / 2 3 2 1
# 2 3 0 3 0 1 0 3 / 2 3 0 3 2 3 2 1

# 0 1 2 1 2 3 2 1 2 3 0 3 2 3 2 1
# 2 3 0 3 0 1 0 3 2 3 0 3 2 3 2 1


# 0 오른
# 1 위
# 2 왼
# 3 아래
# cnt = 0
# for i in range(N):
#     y, x, d, g = list(map(int, input().split()))
#     curve[x][y] = 1
#     queue = [d]
#     queue2 = [d]
#     for j in range(g + 1):
#         for d in queue:
#             x += dx[d]
#             y += dy[d]
#             curve[x][y] = 1
#         queue = [(k+1) % 4 for k in queue2]
#         queue.reverse()
#         queue2 = queue2 + queue
#         # print(queue)
#         # print(queue2)
#
# for i in range(100):
#     for j in range(100):
#         if curve[i][j] and curve[i][j+1] and curve[i+1][j] and curve[i+1][j+1]:
#             cnt += 1
#
# print(cnt)

N = int(input())
curve = [[0 for _ in range(101)] for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def solve(cx, cy, cd, cg):
    curve[cx][cy] = 1
    queue = [cd]
    queue2 = [cd]
    for j in range(cg + 1):
        for di in queue:
            cx += dx[di]
            cy += dy[di]
            curve[cx][cy] = 1
        queue = [(k + 1) % 4 for k in queue2]
        queue.reverse()
        queue2 = queue2 + queue

cnt = 0
for i in range(N):
    y, x, d, g = list(map(int, input().split()))
    solve(x, y, d, g)

for i in range(100):
    for j in range(100):
        if curve[i][j] and curve[i][j+1] and curve[i+1][j] and curve[i+1][j+1]:
            cnt += 1

print(cnt)

