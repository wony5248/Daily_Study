from collections import deque
n = int(input())

start, end = map(int, input().split())
family = [[0 for _ in range(n+1)] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
m = int(input())

def bfs(x):
    queue = deque()
    queue.append(x)
    visit[x] = 1
    count = 0
    while queue:
        count += 1
        for _ in range(len(queue)):
            x = queue.popleft()
            if x == end:
                return count-1
            for i in family[x]:
                if not(visit[i]):
                    visit[i] = 1
                    queue.append(i)
    return -1
for i in range(m):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)



print(bfs(start))