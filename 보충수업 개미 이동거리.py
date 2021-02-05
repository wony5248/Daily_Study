TC = int(input())

for i in range(TC):
    dir = 0
    N = int(input())
    land = [[0 for _ in range(N)] for _ in range(N)]
    for j in range(N):
        land[j] = map(int,  input().split())
