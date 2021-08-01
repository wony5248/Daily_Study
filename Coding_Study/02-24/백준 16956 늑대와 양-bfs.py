from collections import deque
R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]

dx= [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

result = 1

def bfs(x, y):
    global result
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == ".":     # 늑대 기준 상하좌우가 .이라면 울타리로 바꿔줌
            graph[nx][ny] = "D"
        if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == "S":     # 늑대 기준 상하좌우에 양이 있다면 result를 0으로
            result = 0



for i in range(R):
    for j in range(C):
        if graph[i][j] =="W":     #현재 위치가 늑대면 bfs로 탐색 -> 자기 자신을 둘러싼 네방향에 울타리 세워줌
            bfs(i, j)

if result == 0:          # 벽을 세워도 못막는 경우
    print(result)
else:
    print(1)
    for i in range(R):
        answer = ""
        for j in range(C):
            answer += graph[i][j]
        print(answer)

