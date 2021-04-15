import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [input() for _ in range(N)]
result = 100000000
tmp = 0
for i in range(N-8+1):            # 8*8 구역씩 탐색
    for j in range(M-8+1):
        iswhite = 0
        isblack = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 1:         # k + l 을 2로 나눈 것이 같은 것끼리 색이 같아야 함
                    if board[k][l] == "W":      # 첫 블럭이 검정 일때 합이 짝수인 블럭들은 흰색이어야 함
                        isblack +=1
                    if board[k][l] == "B":      # 합이 홀수라면 검정이어야 함
                        iswhite +=1
                else:                      # 첫 블럭이 하양 일때
                    if board[k][l] == "W":
                        iswhite += 1
                    if board[k][l] == "B":
                        isblack += 1
        tmp = min(iswhite, isblack)      # 다 정상적으로 되어 있으면 둘중 하나는 0   -> 둘중 작은 값이 바꿔야 하는 블럭 수
        if result > tmp:
            result = tmp
print(result)