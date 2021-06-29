# from itertools import combinations
# N, M = map(int, input().split())
# result = []
# for i in range(1, N+1):
#     result.append(i)
# lst = list(combinations(result, M))
#
# for i in range(len(lst)):
#     print(" ".join(map(str, lst[i])))

N, M = map(int, input().split())



visit = [0 for _ in range(N+1)]
result = []

def solve(x):
    if x == M:
        print(" ".join(map(str, result)))
        return
    for i in range(1, N+1):
        if visit[i] == 0:
            visit[i] = 1
            result.append(i)
            solve(x+1)
            result.pop()
            for j in range(i+1, N+1):
                visit[j] = 0





solve(0)

