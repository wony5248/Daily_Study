import sys
input = sys.stdin.readline
star = [list(input().rstrip()) for _ in range(5)]
# lst = [chr(i) for i in range(65, 77)]
visit = [0 for _ in range(12)]
coord = [[0, 0] for _ in range(12)]
cnt = 0
istrue = 0


def solve(choose):
    global istrue
    if choose == cnt:
        if ord(star[0][4]) + ord(star[1][3]) + ord(star[2][2]) + ord(star[3][1]) - 256 == 26 and \
                ord(star[0][4]) + ord(star[1][5]) + ord(star[2][6]) + ord(star[3][7]) - 256 == 26 and \
                ord(star[1][1]) + ord(star[1][3]) + ord(star[1][5]) + ord(star[1][7]) - 256 == 26 and \
                ord(star[1][1]) + ord(star[2][2]) + ord(star[3][3]) + ord(star[4][4]) - 256 == 26 and \
                ord(star[3][1]) + ord(star[3][3]) + ord(star[3][5]) + ord(star[3][7]) - 256 == 26 and \
                ord(star[1][7]) + ord(star[2][6]) + ord(star[3][5]) + ord(star[4][4]) - 256 == 26:
            istrue = 1
            return
        else:
            return
    else:
        for i in range(12):
            if visit[i]:
                continue
            else:
                visit[i] = 1
                star[coord[choose][0]][coord[choose][1]] = chr(ord("A") + i)
                solve(choose + 1)
                if istrue:
                    return
                star[coord[choose][0]][coord[choose][1]] = "x"
                visit[i] = 0


for i in range(5):
    for j in range(9):
        if 65 <= ord(star[i][j]) and ord(star[i][j]) <= 76:
            visit[ord(star[i][j]) - 65] = 1
        if star[i][j] == "x":
            coord[cnt][0] = i
            coord[cnt][1] = j
            cnt += 1

solve(0)

for i in range(5):
    print("".join(star[i]))
