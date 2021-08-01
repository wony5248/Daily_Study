# dfs & backtracking

T = int(input())


def solve(count, x, y, distance):
    global result
    if result < distance:     # 가지치기 result보다 크면 볼 가치 없음
        return
    if count == N:            # 끝까지 다 탐색 했다면
        distance += abs(x - end[0]) + abs(y - end[1])    #지금까지 거리 + 집까지의 거리
        result = min(distance, result)                   # result와 비교해서 더 작은값 가져감
        return
    for j in range(2, N+2):
        if visit[j] == 0:
            visit[j] = 1
            com = distance + abs(x - location[j][0]) + abs(y - location[j][1])    # 각 고객과의 거리 누적 합
            solve(count +1, location[j][0], location[j][1], com)                  # 다음 고객 재귀 - dfs 탐색
            visit[j] = 0

for i in range(T):
    N = int(input())
    visit = [0 for _ in range(N+2)]
    x = list(map(int, input().split()))
    location = []
    for j in range(0, len(x), 2):
        location.append([x[j], x[j+1]])

    start = location[0]
    end = location[1]
    result = 2000
    solve(0, start[0], start[1], 0)

    print("#%d %d" % (i+1, result))


