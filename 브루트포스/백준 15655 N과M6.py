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
#         if result and result[-1] < lst[i] :
#             result.append(lst[i])
#
#             solve(x + 1)
#             result.pop()
#
#         elif not result :
#             result.append(lst[i])
#
#             solve(x + 1)
#             result.pop()
#
#
#
# solve(0)
#

N, M = map(int, input().split())
lst = list(map(int,input().split()))
visit = [0 for _ in range(N)]
result = []
lst.sort()
def solve(x):
    if x == M:
        print(" ".join(map(str, result)))
        return
    for i in range(N):
        if visit[i] == 0:
            result.append(lst[i])
            visit[i] = 1
            solve(x + 1)
            result.pop()
            for j in range(i+1, N):
                visit[j] = 0



solve(0)