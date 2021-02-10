N = int(input())
graph = [[] for _ in range(2)]
graph[0].append([0])
graph[1].append([0])
result = []

def dfs(start, end):
    visit[start] = 1
    for j in graph[1][start]:
        if visit[j] == 0:
            dfs(j, end)
        elif visit[j] == 1 and j == end:
            result.append(j)


for i in range(1, N+1):
    graph[0].append([i])
    num = int(input())
    graph[1].append([num])


for i in range(1, N+1):
    visit = [0 for _ in range(N+1)]
    dfs(i, i)
print(len(result))
for i in result:
    print(i)

