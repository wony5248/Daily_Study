from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
board = [0 for _ in range(101)]
lad = [0 for _ in range(101)]

check = [0 for _ in range(101)]

def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        cx = queue.popleft()
        for d in range(1, 7):           # 주사위 1~ 6 굴리는거
            nx = cx + d
            if 0 <= nx < 101 and lad[nx]:        # 보드판 범위 안이고 사다리나 뱀이라면
                nnx = lad[nx]                    # 사다리나 뱀을 탔을때의 위치
                if not check[nnx]:               # 방문하지 않았었으면 현재 까지 주사위 굴린 수 +1
                    check[nnx] = check[cx] + 1
                    queue.append(nnx)
                elif check[nnx] and check[nnx] > check[cx] + 1:    # 방문은 했었으나 지금이 더 덜 굴리고 올수 있다면
                    check[nnx] = check[cx] + 1                     # 굴린 횟수 바꿔줌
            elif 0 <= nx < 101:                     # 사다리나 뱀이 아니면
                if not check[nx]:
                    check[nx] = check[cx] + 1
                    queue.append(nx)
                elif check[nx] and check[nx] > check[cx] + 1:
                    check[nx] = check[cx] + 1
                    queue.append(nx)




for i in range(N + M):
    x, y = map(int, input().rstrip().split())
    lad[x] = y                                          # 뱀이랑 사다리 어디로 이동하는지


bfs(1)



print(check[100])