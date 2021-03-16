import sys
N, M, K = map(int, sys.stdin.readline().split())
price = list(map(int, sys.stdin.readline().split()))
def find(x):
    if parent[x] == x:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        cost[x] = cost[y] + cost[x]






parent = [0 for _ in range(N+1)]
cost = [0 for _ in range(N+1)]


for j in range(M):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    if x not in parent:
        parent[x] = x
        cost[x] = price[x-1]
    if y not in parent:
        parent[y] = y
        cost[y] = price[x-1]

        union(x, y)
print(parent)
print(cost)
print(price)
