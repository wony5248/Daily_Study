from collections import deque
TC = int(input())


def backtracking(x, value):
    global result

    if value <= result:
        return
    if x >= N:
        result = value
        return

    for k in range(N):
        if not check[k]:
            check[k] = 1
            backtracking(x+1, value * lst[x][k])
            check[k] = 0


for i in range(1, TC+1):
    N = int(input())
    lst = [[0 for _ in range(N)] for _ in range(N)]
    store = [[] for _ in range(N)]
    queue = deque()
    result = 0
    for j in range(N):
        lst[j] = list(map(lambda x : int(x) / 100, input().split()))
    check = [0 for _ in range(N)]
    backtracking(0, 100)

    print("#%d %.6f" %(i, result))