import copy
import sys
from collections import deque
input = sys.stdin.readline
INF = float("INF")

# 동 서 남 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
directions = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[0, 2], [2, 1], [1, 3], [3, 0]],
             [[3, 0, 2], [1, 3, 0], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]]

def watch(x, y, direction, temp):
    for d in direction:
        nx = x
        ny = y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and temp[nx][ny] != 6:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = '#'
            else:
                break

def dfs(office, cnt):
    global ans

    temp = copy.deepcopy(office)
    if cnt == cctv_cnt:
        c = 0
        for i in temp:
            c += i.count(0)
        ans = min(ans, c)
        return
    x, y, cctv = q[cnt]
    for dir in directions[cctv]:
        watch(x, y, dir, temp)
        dfs(temp, cnt + 1)
        temp = copy.deepcopy(office)

n, m = map(int, input().split())
office = []
cctv_cnt = 0
q = deque()
ans = INF
for i in range(n):
    input_data = list(map(int, input().split()))
    office.append(input_data)
    for j in range(len(input_data)):
        if input_data[j] != 0 and input_data[j] != 6:
            cctv_cnt += 1
            q.append([i, j, input_data[j]])

dfs(office, 0)
print(ans)