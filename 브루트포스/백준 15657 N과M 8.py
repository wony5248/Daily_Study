N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

result = []
def solve(x):
    if x == M:
        print(" ".join(map(str, result)))
        return
    for i in range(N):
        if result and result[-1] <= lst[i]:
            result.append(lst[i])
            solve(x+1)
            result.pop()
        elif not result:
            result.append(lst[i])
            solve(x + 1)
            result.pop()

solve(0)