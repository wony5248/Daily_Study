T = int(input())
for i in range(T):

    N, M = map(int, input().split())   # 흑 1  백 2
    chess = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    cen = N // 2
    chess[cen][cen] =2
    chess[cen+1][cen+1] = 2
    chess[cen][cen+1] = 1
    chess[cen+1][cen] = 1

    for j in range(M):
        x, y, color = map(int, input().split())

    for j in range(N+1):
        print(chess[j])