import sys
T = int(sys.stdin.readline().rstrip())

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
        num[x] = num[y] + num[x]




for i in range(T):
    F = int(sys.stdin.readline().rstrip())
    parent = {}
    num = {}
    for j in range(F):
        x, y = sys.stdin.readline().rstrip().split()
        if x not in parent:
            parent[x] = x
            num[x] = 1
        if y not in parent:
            parent[y] = y
            num[y] = 1

        union(x, y)
        print(num[find(x)])