N = int(input())
count = 0
area = [[0 for _ in range(100)] for _ in range(100)]
for i in range(N):
    x, y = map(int, input().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            area[j][k] = 1
for i in range(100):
    for j in range(100):
        if area[i][j] == 1:
            count += 1

print(count)