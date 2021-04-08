import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [input() for _ in range(N)]
result = 100000000
tmp = 0
for i in range(N-8+1):
    for j in range(M-8+1):
        iswhite = 0
        isblack = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 1:
                    if board[k][l] == "W":
                        iswhite +=1
                    if board[k][l] == "B":
                        isblack +=1
                else:
                    if board[k][l] == "W":
                        isblack += 1
                    if board[k][l] == "B":
                        iswhite += 1
        tmp = min(iswhite, isblack)

        if result > tmp:
            result = tmp
print(result)