graph = [[0 for _ in range(100)] for _ in range(100)]
for i in range(4):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(ry - ly):
        for j in range(rx - lx):
            graph[lx + j][ly + i] = 1
count = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1:
            count += 1

print(count)