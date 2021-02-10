import sys
N, M = map(int, sys.stdin.readline().split())
lst = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    lst[i] = list(map(int, sys.stdin.readline().split()))




copylst = [0 for _ in range(N + 1)]
    for i in range(1, N + 1):
        copylst[i] = copylst[i - 1] + lst[i - 1]
    for i in range(M):
        x, y = map(int, sys.stdin.readline().split())

        print(copylst[y] - copylst[x - 1])