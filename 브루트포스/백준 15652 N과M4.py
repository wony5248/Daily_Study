# from itertools import permutations
# N, M = map(int, input().split())
# result = []
# for i in range(1, N+1):
#     result.append(i)
# lst = list(permutations(result, M))
#
# for i in range(len(lst)):
#     print(" ".join(map(str, lst[i])))

N, M = map(int, input().split())
result = []


def solve(x):
    if x == M:
        print(" ".join(map(str, result)))
        return
    for i in range(1, N+1):
        if result and i >= result[-1]:
            result.append(i)
            solve(x+1)
            result.pop()
        elif not result:
            result.append(i)
            solve(x+1)
            result.pop()


solve(0)

