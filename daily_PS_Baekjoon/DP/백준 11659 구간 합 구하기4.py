
import sys
N, M = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))

copylst = [0 for _ in range(N+1)]
for i in range(1, N+1):
    copylst[i] = copylst[i-1] + lst[i-1]
for i in range(M):

    x, y = map(int, sys.stdin.readline().split())


    print(copylst[y] - copylst[x-1])



# N, M = map(int, input().split())
#
# lst = list(map(int, input().split()))
#
#
#
# for i in range(M):
#     result = 0
#     copy = [0 for _ in range(N)]
#     x, y = map(int, input().split())
#     for j in range(len(lst)):
#         copy[j] =lst[j]
#     for j in range(1, len(copy)):
#         copy[j] += copy[j - 1]
#     if x >= 2:
#         result = copy[y-1] - copy[x-2]
#     else:
#         result = copy[y-1]
#     print(result)