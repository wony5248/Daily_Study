omok = [list(map(int, input().split())) for _ in range(19)]
print(omok)
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

answer = 0
result = []
def solve(x, y, cnt, res, arr):
    cx = x
    cy = y
    arr2 = arr

    print("hi")


for i in range(19):
    for j in range(19):
        if omok[i][j] == 1:
            for d in range(8):
            solve(i, j, 1, 1, [[i, j]])