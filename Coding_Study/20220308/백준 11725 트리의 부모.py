from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
tree = [[] for _ in range(N+1)]
visit = [0 for _ in range(N+1)]
node = [0 for _ in range(N+1)]
queue = deque()


def bfs(start):
    queue.append(start)
    while queue:
        start = queue.popleft()
        for j in tree[start]:
            if visit[j] == 0:
                queue.append(j)
                visit[j] = 1
                node[j] = start


for i in range(N-1):
    parent, child = list(map(int, input().split()))
    tree[parent].append(child)
    tree[child].append(parent)
bfs(1)
for i in range(2,N+1):
    print(node[i])


