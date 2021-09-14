import sys
input = sys.stdin.readline
N, M = map(int, input().split())
light = [[] for _ in range(N+1)]
heavy = [[] for _ in range(N+1)]
high = []
low = []
result = 0
def dfs(x):
    global cnt
    visit[x] = 1
    for j in light[x]:
        if visit[j] == 0:
            dfs(j)
            cnt += 1


def dfs1(x):
    global cnt1
    visit1[x] = 1
    for j in heavy[x]:
        if visit1[j] == 0:
            dfs1(j)
            cnt1 += 1


for i in range(M):
    x, y = map(int, input().split())
    light[x].append(y)
    heavy[y].append(x)


for i in range(1, N+1):
    visit = [0 for _ in range(N + 1)]
    visit1 = [0 for _ in range(N+1)]
    cnt1 = 0
    cnt = 0
    dfs(i)
    dfs1(i)
    high.append(cnt)
    low.append(cnt1)
for i in range(N):
    if high[i] > N // 2:
        result += 1
    if low[i] > N //2 :
        result += 1
print(result)
