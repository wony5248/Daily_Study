move = [(-1,0),(1,0),(0,1),(0,-1)]
N, M, T = map(int, input().split())
castle = []
visited = [[0 for _ in range(M)] for _ in range(N)]
gram = False
success = -1
for _ in range(N):
    castle.append(input().split())

def get_distance(y,x):
    return abs(N-y-1)+abs(M-x-1)

# time, loc(y,x)
q = [(0,0,0)]
visited[0][0] = 1
route = float("inf")
while len(q):
    time, y, x = q.pop(0)
    if y == N-1 and x == M-1:
        success = min(time, route)
        break
    if time == T+1:
        break
    else:
        for i,j in move:
            yy = y+i
            xx = x+j
            if 0<=yy<N and 0<=xx<M and castle[yy][xx] != '1' and not visited[yy][xx]:
                visited[yy][xx] = 1
                q.append((time+1, yy,xx))
                if castle[yy][xx] == '2':
                    route = time + get_distance(yy, xx) + 1
                    success = route


if 0 <= success <= T:
    print(success)
else:
    print("Fail")