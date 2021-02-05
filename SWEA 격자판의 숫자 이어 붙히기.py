# import sys
# sys.setrecursionlimit(20000000)
# TC = int(input())
# dx = [0, -1, 0, 1]
# dy = [-1, 0, 1, 0]
# graph = [[0 for _ in range(4)] for _ in range(4)]
#
# def dfs(x, y, num):
#     if len(num) == 7:
#         result.add(num)
#         return
#     for l in range(4):
#         nx = x + dx[l]
#         ny = y + dy[l]
#         if 0 <= nx < 4 and 0 <= ny < 4:
#             dfs(nx, ny, num + graph[nx][ny])
#
#
#
# for i in range(1, TC+1):
#     for j in range(4):
#         graph[j] = list(input().split())
#     result = set()
#     for j in range(4):
#         for k in range(4):
#             dfs(j, k, "")
#     print("#%d %d" %(i, len(result)))
import sys
from collections import deque
s = input


def solution(graph):
    answer = set()
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    for x in range(0, 4):
        for y in range(0, 4):
            start = (x, y, graph[x][y])

            q = deque([start])

            while q:
                cur_x, cur_y, cur_num = q.popleft()

                for i in range(4):
                    nx = cur_x + dx[i]
                    ny = cur_y + dy[i]

                    if 0 <= nx < 4 and 0 <= ny < 4:
                        if len(cur_num) < 6:
                            q.append((nx, ny, cur_num+graph[nx][ny]))
                        else:
                            answer.add(cur_num+graph[nx][ny])

    return len(answer)


if __name__ == "__main__":
    N = int(s())
    for n in range(1, N+1):
        Graph = [list(s().split()) for _ in range(4)]
        print("#%d %d" % (n, solution(Graph)))