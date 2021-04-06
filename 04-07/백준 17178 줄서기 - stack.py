N = int(input())
row = [list(input().rstrip().split()) for _ in range(N)]
wait = []

wait.append(row[0][0])
for i in range(N):
    for j in range(4):
        if i == 1 and j == 1:
            continue
        elif j != 3:
            if wait[-1][0] > row[i][j][0] and row[i][j][0] > row[i][j+1][0]:





