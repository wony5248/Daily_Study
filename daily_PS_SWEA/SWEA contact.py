from collections import deque

def bfs(x):
    visit[x] = 1
    queue.append(x)

    while queue:
        x = queue.popleft()
        for j in range(1, 101):
            if rel[x][j] == 1 and visit[j] ==0:
                visit[j] = 1
                queue.append(j)
                dis[j] = dis[x] + 1



for i in range(1, 11):
    rel = [[0 for _ in range(101)] for _ in range(101)]
    visit = [0 for _ in range(101)]
    dis = [0 for _ in range(101)]
    length, start = map(int, input().split())
    x = list(map(int, input().split()))
    for j in range(0, length, 2):
        rel[x[j]][x[j+1]] = 1
    queue = deque()
    bfs(start)

    maxdis = dis[0]
    for k in range(1, len(dis)):
        if maxdis <= dis[k]:
            maxdis = dis[k]
            index = k
    print("#%d %d" %(i, index))