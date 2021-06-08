import sys
N, B = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

def solve(mat, B):
    if B == 1:
        for i in range(N):
            for j in range(N):
                mat[i][j] %= 1000
        return mat
    elif B % 2 == 0:
        mat2 = [[0 for _ in range(N)] for _ in range(N)]
        recmat = solve(mat, B//2)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    mat2[i][j] += recmat[i][k] * recmat[k][j]
                mat2[i][j] %= 1000
        return mat2
    else:
        mat2 = [[0 for _ in range(N)] for _ in range(N)]
        recmat = solve(mat, B-1)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    mat2[i][j] += recmat[i][k] * mat[k][j]
                mat2[i][j] %= 1000
        return mat2

result = solve(mat, B)

for i in result:
    for j in i:
        print(j, end=" ")
    print()