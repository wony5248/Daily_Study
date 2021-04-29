import sys
input = sys.stdin.readline
N, r, c= map(int, input().split())
arr = [[0 for _ in range(2 ** N)] for _ in range(2 ** N)]
rsize = 2 ** N
divide = 2 ** (N-1)
check = 0

def solve(x, y, size):
    global check
    if size == 2:
        for i in range(x, x + size):
            for j in range(y, y + size):
                arr[i][j] = check
                check += 1
    else:
        solve(x, y, size // 2)  # 1사분면
        solve(x, y + size // 2, size // 2)  # 2사분면
        solve(x + size // 2, y, size // 2)  # 3사분면
        solve(x + size // 2, y + size // 2, size // 2)

solve(0, 0, 2 ** N)
print(arr[r][c])
for i in range(2**N):
    print(arr[i])








