n = int(input())
tri = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    tri[i] = list(map(int, input().split()))


num = 2
for i in range(1, n):
    for j in range(num):
        if j == 0:
            tri[i][j] += tri[i-1][j]
        elif i == j:
            tri[i][j] += tri[i-1][j-1]
        else:
            choose = max(tri[i-1][j-1], tri[i-1][j])
            tri[i][j] += choose
    num += 1
print(max(tri[n-1]))