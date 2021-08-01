# 6 = 2 2 = 6
import sys
# input = sys.stdin.readline
gear = [list(map(int, input())) for _ in range(4)]
K = int(input())
result = 0
for i in range(K):
    gnum, gdir = list(map(int, input().split()))
    if gnum == 1 and gdir == 1:          # 1번 시계방향
        if gear[0][2] != gear[1][6]:                  # 각각 맞물리는 톱니 극이  다를때
            if gear[1][2] != gear[2][6]:
                if gear[2][2] != gear[3][6]:
                    gear[3].append(gear[3].pop(0))          # 반시계 방향
                gear[2].insert(0, gear[2].pop())            # 시계방향
            gear[1].append(gear[1].pop(0))                  # 반시계 방향
        gear[0].insert(0, gear[0].pop())                    # 시계 방향

    elif gnum == 1 and gdir == -1:         # 1번 반시계 방향
        if gear[0][2] != gear[1][6]:
            if gear[1][2] != gear[2][6]:
                if gear[2][2] != gear[3][6]:
                    gear[3].insert(0, gear[3].pop())
                gear[2].append(gear[2].pop(0))
            gear[1].insert(0, gear[1].pop())
        gear[0].append(gear[0].pop(0))

    if gnum == 2 and gdir == 1:          # 2번 시계 방향
        if gear[1][6] != gear[0][2]:
            gear[0].append(gear[0].pop(0))
        if gear[1][2] != gear[2][6]:
            if gear[2][2] != gear[3][6]:
                gear[3].insert(0, gear[3].pop())
            gear[2].append(gear[2].pop(0))
        gear[1].insert(0, gear[1].pop())

    elif gnum == 2 and gdir == -1:       # 2번 반 시계
        if gear[1][6] != gear[0][2]:
            gear[0].insert(0, gear[0].pop())
        if gear[1][2] != gear[2][6]:
            if gear[2][2] != gear[3][6]:
                gear[3].append(gear[3].pop(0))
            gear[2].insert(0, gear[2].pop())
        gear[1].append(gear[1].pop(0))

    elif gnum ==3 and gdir == 1:           # 3번 시계 방향
        if gear[2][2] != gear[3][6]:
            gear[3].append(gear[3].pop(0))
        if gear[1][2] != gear[2][6]:
            if gear[0][2] != gear[1][6]:
                gear[0].insert(0, gear[0].pop())
            gear[1].append(gear[1].pop(0))
        gear[2].insert(0, gear[2].pop())

    elif gnum ==3 and gdir == -1:           # 3번 반시계 방향
        if gear[2][2] != gear[3][6]:
            gear[3].insert(0, gear[3].pop())
        if gear[1][2] != gear[2][6]:
            if gear[0][2] != gear[1][6]:
                gear[0].append(gear[0].pop(0))
            gear[1].insert(0, gear[1].pop())
        gear[2].append(gear[2].pop(0))

    elif gnum == 4 and gdir == 1:          # 4번 시계 방향
        if gear[3][6] != gear[2][2]:
            if gear[2][6] != gear[1][2]:
                if gear[1][6] != gear[0][2]:
                    gear[0].append(gear[0].pop(0))
                gear[1].insert(0, gear[1].pop())
            gear[2].append(gear[2].pop(0))
        gear[3].insert(0, gear[3].pop())

    elif gnum == 4 and gdir == -1:         # 4번 반시계 방향
        if gear[3][6] != gear[2][2]:
            if gear[2][6] != gear[1][2]:
                if gear[1][6] != gear[0][2]:
                    gear[0].insert(0, gear[0].pop())
                gear[1].append(gear[1].pop(0))
            gear[2].insert(0, gear[2].pop())
        gear[3].append(gear[3].pop(0))

if gear[0][0] == 1:
    result += 1
if gear[1][0] == 1:
    result += 2
if gear[2][0] == 1:
    result += 4
if gear[3][0] == 1:
    result += 8


print(result)