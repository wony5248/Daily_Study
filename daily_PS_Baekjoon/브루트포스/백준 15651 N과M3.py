#
# from itertools import product
# N, M = map(int, input().split())
# result = []
# for i in range(1, N+1):
#     result.append(i)
# lst = list(product(result, repeat=M))
#
# for i in range(len(lst)):
#     print(" ".join(map(str, lst[i])))
#
#




N, M = map(int, input().split())



visit = [0 for _ in range(N+1)]
result = []

def solve(x):
    if x == M:
        print(" ".join(map(str, result)))
        return
    for i in range(1, N+1):
        if visit[i] == 0:

            result.append(i)
            solve(x+1)
            result.pop()






solve(0)

