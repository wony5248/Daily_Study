import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = float("inf")
lst = [[INF for _ in range(n)] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if c < lst[a-1][b-1]:
        lst[a-1][b-1] = c


for l in range(n):
    for j in range(n):
        for k in range(n):
            if j != k and lst[j][k] > lst[j][l] + lst[l][k]:
                lst[j][k] = lst[j][l] + lst[l][k]

for i in range(n):
    for j in range(n):
        if lst[i][j] == INF:
            print(0, end=" ")
        else:
            print(lst[i][j], end=" ")
    print()