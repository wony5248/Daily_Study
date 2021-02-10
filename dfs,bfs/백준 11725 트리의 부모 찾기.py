from collections import deque
import sys
sys.setrecursionlimit(20000000)
N = int(input())
tree = [[] for _ in range(N+1)]
visit = [0 for _ in range(N+1)]
result = [0 for _ in range(N+1)]

# def bfs(start):
#     queue = deque()
#     queue.append(start)
#     while queue:
#         start = queue.popleft()
#         for j in tree[start]:
#             if visit[j] == 0:
#                 queue.append(j)
#                 visit[j] = 1
#                 result[j] = start

def dfs(start):
    for j in tree[start]:
        if visit[j] == 0:
            visit[j] = 1
            result[j] = start
            dfs(j)


for i in range(N-1):
    parent, son = list(map(int, input().split()))
    tree[parent].append(son)
    tree[son].append(parent)
# bfs(1)
dfs(1)
for i in range(2,N+1):
    print(result[i])


