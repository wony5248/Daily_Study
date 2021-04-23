import sys
input = sys.stdin.readline
N, r, c= map(int, input().split())
arr = [[0 for _ in range(2 ** N)] for _ in range(2 ** N)]
rsize = 2 ** N
divide = 2 ** (N-1)
check = 0

def solve(x, y, size):
    global check
    for i in range(x, x + size):
        for j in range(y, y + size):
            arr[i][j] = check
            check += 1

solve(0, 0, 2)
for i in range(rsize):
    print(arr[i])
if 0 <= r < divide and 0 <= c < divide:
    print(arr[r][c])
elif 0 <= r < divide and 2 ** (N-1) <= c < rsize:
    print(arr[r][c - divide] + (rsize * rsize) // 4)
elif divide <= r < rsize and 0 <= c <divide:
    print(arr[r - divide][c] + (rsize * rsize) // 4 * 2)
else:
    print(arr[r - divide][c - divide] + (rsize * rsize) // 4 * 3)







