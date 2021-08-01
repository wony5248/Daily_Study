import sys
from collections import deque

sys.setrecursionlimit(20000000)
input = sys.stdin.readline

FF, FS, SF, SS = map(int, input().split())

song = []
answer = 0
front = []
isf = 0


def solve(x, count):
    queue = deque()
    global answer
    queue.append([x, count])
    if count == len(song):
        return
    while queue:
        print(queue)

        cx, ccount = queue.popleft()
        if answer < ccount:
            answer = ccount
        if ccount == len(song):
            break
        for j in range(len(song)):
            if cx[-1] == song[j][0] and visit[j] == 0:
                queue.append([cx + song[j], ccount + 1])
                visit[j] = 1

    return


for i in range(FF):
    song.append("FF")
    isf += 1
for i in range(FS):
    song.append("FS")
    isf += 1
for i in range(SF):
    song.append("SF")
for i in range(SS):
    song.append("SS")

if isf:
    for i in range(len(song)):
        visit = [0 for _ in range(len(song))]
        if song[i][0] == "F":
            visit[i] = 1
            solve(song[i], 1)
    print(answer)
else:
    for i in range(len(song)):
        visit = [0 for _ in range(len(song))]
        visit[i] = 1
        solve(song[i], 1)
    print(answer)





