from collections import deque
N, M, x, y, K = map(int, input().split())
guide = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))
dir = {
    1: [0, 1],     # 동
    2: [0, -1],    # 서
    3: [-1, 0],    # 북
    4: [1, 0],     # 남
}
dice = [0,0,0,0,0,0]
#dice[0] = 바닥 dice[5]는 윗면  - 고정
#dice[1] dice[4] 는 위아래 이동시 사용 -> 세로
#dice[2] dicw[3] 은 좌우 이동시 사용 -> 가로

def solve(sx, sy):
    for i in range(K):
        if command[i] == 4:          # 남쪽 이동
            nx = sx + dir[4][0]
            ny = sy + dir[4][1]
            if 0 <= nx < N and 0 <= ny < M:      # 좌표 안에 있다면 주사위 굴려줌
                dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]   #주사위를 남쪽 이동했을때의 모습으로 바꿔줌
                if guide[nx][ny] == 0:        # 바닥이 0 이면
                    guide[nx][ny] = dice[0]   # 주사위 숫자 바닥에 넣어줌
                else:                         # 바닥이 0이 아닐 시
                    dice[0] = guide[nx][ny]   # 주사위에 바닥 숫자 넣어줌
                    guide[nx][ny] = 0
                sx = nx
                sy = ny
                print(dice[5])
        elif command[i] == 3:   # 북쪽 이동
            nx = sx + dir[3][0]
            ny = sy + dir[3][1]
            if 0 <= nx < N and 0 <= ny < M:
                dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
                if guide[nx][ny] == 0:
                    guide[nx][ny] = dice[0]
                else:
                    dice[0] = guide[nx][ny]
                    guide[nx][ny] = 0
                sx = nx
                sy = ny
                print(dice[5])
        elif command[i] == 2:
            nx = sx + dir[2][0]
            ny = sy + dir[2][1]
            if 0 <= nx < N and 0 <= ny < M:
                dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
                if guide[nx][ny] == 0:
                    guide[nx][ny] = dice[0]
                else:
                    dice[0] = guide[nx][ny]
                    guide[nx][ny] = 0
                sx = nx
                sy = ny
                print(dice[5])
        elif command[i] == 1:
            nx = sx + dir[1][0]
            ny = sy + dir[1][1]
            if 0 <= nx < N and 0 <= ny < M:
                dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
                if guide[nx][ny] == 0:
                    guide[nx][ny] = dice[0]
                else:
                    dice[0] = guide[nx][ny]
                    guide[nx][ny] = 0
                sx = nx
                sy = ny
                print(dice[5])



solve(x, y)



