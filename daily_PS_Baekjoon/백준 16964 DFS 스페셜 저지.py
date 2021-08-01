import sys
sys.setrecursionlimit(200000)
N = int(input())
tree = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
visit = [0 for _ in range(N + 1)]
result = []

def dfs(start):
    visit[start] = 1
    result.append(start)
    for j in range(1, N+1):
        if tree[start][j] and visit[j] == 0:
            visit[j] = 1
            dfs(j)




for i in range(N - 1):
    x, y = map(int, input().split())
    tree[x][y] = 1

order = list(map(int, input().split()))
dfs(1)

if result == order:
    print(1)
else:
    print(0)