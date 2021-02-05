N, M = map(int, input().split())
r, c, d = map(int, input().split())
dx = [0, ]
dy = []
area = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    x = list(map(int, input().split()))
    area[i] = x
dfs(r-1, c-1)
print(area)
