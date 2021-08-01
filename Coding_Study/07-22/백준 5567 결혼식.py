from collections import deque
N = int(input())
M = int(input())
friends = [[0 for _ in range(N+1)] for _ in range(N+1)]
visit = [0 for _ in range(N+1)]
cnt = 0
start = deque()
answer = deque()
def bfs(lst):
    while lst:
        x = lst.popleft()
        for i in range(2, N+1):
            if friends[x][i]:
                answer.append(i)

for i in range(M):
    a, b = list(map(int, input().split()))
    if a == 1:
        start.append(b)
        answer.append(b)
    friends[a][b] = 1
    friends[b][a] = 1

bfs(start)
print(len(set(answer)))

