import sys
sys.setrecursionlimit(500000)

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])

        return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y






n, m = map(int, sys.stdin.readline().rstrip().split())
parent = [i for i in range(n + 1)]

for j in range(m):
    oper, x, y = map(int, sys.stdin.readline().rstrip().split())

    if oper == 0:
        union(x, y)
    elif oper == 1:
        if find(x) == find(y):
            print("YES")
        else:
            print("NO")

