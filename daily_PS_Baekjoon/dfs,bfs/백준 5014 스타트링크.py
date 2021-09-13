from collections import deque
import sys
input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())
stage = [0 for _ in range(F+1)]
visit = [0 for _ in range(F+1)]
check = [0 for _ in range(F+1)]
isflag = 0

def bfs(x):
    queue = deque()
    global isflag
    queue.append(x)
    visit[x] = 1
    while queue:
        cx = queue.popleft()
        if cx == G:
            isflag = 1
            break
        if 1 <= cx + U <= F and visit[cx + U] == 0:
            visit[cx + U] = 1
            if check[cx + U] == 0:
                check[cx + U] = check[cx] + 1
            else:
                check[cx + U] = min(check[cx + U], check[cx] + 1)
            queue.append(cx + U)
        if 1 <= cx - D <= F and visit[cx - D] == 0:
            visit[cx - D] = 1
            if check[cx - D] == 0:
                check[cx - D] = check[cx] + 1
            else:
                check[cx - D] = min(check[cx - D], check[cx] + 1)
            queue.append(cx - D)


bfs(S)
if check[G] or isflag:
    print(check[G])
else:
    print("use the stairs")