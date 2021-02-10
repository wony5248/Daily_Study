N, M = map(int, input().split())
A = [[0 for _ in range(M)] for _ in range(N)]
B = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    A[i] = list(map(int, input()))
for i in range(N):
    B[i] = list(map(int, input()))

def change(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1 -A[i][j]


def check():
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                return 0
    return 1

count = 0

for i in range(0, N-2):
    for j in range(0, M-2):
        if A[i][j] != B[i][j]:
            change(i, j)
            count += 1

if check():
    print(count)
else:
    print(-1)

