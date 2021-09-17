import sys
input = sys.stdin.readline
N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]

eye = [1, 2, 3, 4, 5, 6]
eye = set(eye)
com = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
top = 0

for j in range(6):
    lst = list()
    sub = []
    se1 = set()
    se1.add(dice[0][j])
    se1.add(dice[0][com[j]])
    sub.append(list(eye - se1))
    lst.append(dice[0][j])
    lst.append(dice[0][com[j]])
    for k in range(1, N):
        idx = dice[k].index(lst[-1])
        se = set()
        se.add(dice[k][idx])
        se.add(dice[k][com[idx]])
        diff = eye - se
        sub.append(list(diff))
        lst.append(dice[k][idx])
        lst.append(dice[k][com[idx]])
    lst = list(set(lst))
    maxV = 0
    for i in range(len(sub)):
        maxV += max(sub[i])
    if top < maxV:
        top = maxV

print(top)