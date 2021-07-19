from itertools import combinations
import sys
input = sys.stdin.readline


def dfs(count):
    global isanswer, win, lose, draw
    if count == 15:
        if win.count(0) == 6 and lose.count(0) == 6 and draw.count(0) == 6:
            isanswer = 1
        return
    x, y = game[count]
    if win[x] > 0 and lose[y] > 0:
        win[x] -= 1
        lose[y] -= 1
        dfs(count + 1)
        win[x] += 1
        lose[y] += 1
    if win[y] > 0 and lose[x] > 0:
        win[y] -= 1
        lose[x] -= 1
        dfs(count + 1)
        win[y] += 1
        lose[x] += 1
    if draw[x] > 0 and draw[y] > 0:
        draw[x] -= 1
        draw[y] -= 1
        dfs(count + 1)
        draw[x] += 1
        draw[y] += 1


game = list(combinations(range(6), 2))
answer = []
for i in range(4):
    match = list(map(int, input().split()))
    win, lose, draw = [], [], []
    for j in range(18):
        if j % 3 == 0:
            win.append(match[j])
        elif j % 3 == 1:
            draw.append(match[j])
        elif j % 3 == 2:
            lose.append(match[j])
    isanswer = 0
    dfs(0)
    answer.append(isanswer)
print(*answer)