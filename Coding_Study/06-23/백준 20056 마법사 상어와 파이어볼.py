import sys
from collections import deque
input = sys.stdin.readline
N, M, K = map(int, input().split())
fireball = [[deque() for _ in range(N)] for _ in range(N)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
queue = deque()
result = 0

def combine():
    for i in range(N):
        for j in range(N):
            if len(fireball[i][j]) > 1:
                nm, ns, isodd, iseven = 0, 0, 0, 0
                for k in range(len(fireball[i][j])):
                    nm += fireball[i][j][k][0]
                    ns += fireball[i][j][k][1]
                    if fireball[i][j][k][2] % 2 == 0:
                        iseven += 1
                    elif fireball[i][j][k][2] % 2 == 1:
                        isodd += 1
                length = len(fireball[i][j])
                nm //= 5
                ns //= length
                fireball[i][j] = deque()
                if nm != 0:
                    for k in range(4):
                        if isodd == length or iseven == length:
                            nd = 2 * k
                        else:
                            nd = (2 * k) + 1
                        fireball[i][j].append([nm, ns, nd])



for i in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball[r-1][c-1].append([m, s, d])
    queue.append([r-1, c-1])


for i in range(K):
    queue2 = []
    for j in range(len(queue)):
        cx, cy = queue.popleft()
        for k in range(len(fireball[cx][cy])):
            print(fireball[cx][cy])
            cm, cs, cd = fireball[cx][cy].popleft()
            nx = (cx + (dx[cd] * cs)) % N
            ny = (cy + (dy[cd] * cs)) % N

            queue.append([nx, ny])
            queue2.append([cm, cs, cd])
    for x, y, m, s, d in queue2:
        fireball[x][y].append([m, s, d])
    combine()


for i in range(N):
    for j in range(N):
        if fireball[i][j]:
            for k in range(len(fireball[i][j])):
                result += fireball[i][j][k][0]


print(result)
