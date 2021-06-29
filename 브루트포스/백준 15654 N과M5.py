

from itertools import permutations
N, M = map(int, input().split())
result = list(map(int,input().split()))
result.sort()
lst = list(permutations(result, M))

for i in range(len(lst)):
    print(" ".join(map(str, lst[i])))





#
# N, M = map(int, input().split())
# lst = list(map(int,input().split()))
# visit = [0 for _ in range(N)]
# result = []
# lst.sort()
# def solve(x):
#     if x == M:
#         print(" ".join(map(str, result)))
#         return
#     for i in range(N):
#         if visit[i] == 0:
#             result.append(lst[i])
#             visit[i] = 1
#             solve(x + 1)
#             visit[i] = 0
#             result.pop()
#
#
# solve(0)