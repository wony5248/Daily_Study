import sys
sys.setrecursionlimit(500000)
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
plan = list(map(int, sys.stdin.readline().split()))

parent = [i for i in range(N + 1)]
isflag =0


def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            union(i+1, j+1)

for i in range(1, len(plan)):
    if find(plan[i]) != find(plan[i-1]):
        isflag = 1


if isflag == 1:
    print("NO")
else:
    print("YES")
print(parent)

