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
while len(q):
    time, y, x = q.pop(0)
    if time == T:
        break
    if y == N-1 and x == M-1:
        success = time
        break
    if gram:
        route = time + get_distance(y,x)
        if route <= T and (route < success or success < 0):
            success = route
        gram = False

    else:
        for i,j in move:
            yy = y+i
            xx = x+j
            if 0<=yy<N and 0<=xx<M and castle[yy][xx] != '1' and not visited[yy][xx]:
                visited[yy][xx] = 1
                q.append((time+1, yy,xx))
                if castle[yy][xx] == '2':
                    gram = True

if success < 0:
    print("Fail")
else:
    print(success)