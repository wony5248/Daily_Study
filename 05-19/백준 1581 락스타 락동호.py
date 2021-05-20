import sys
sys.setrecursionlimit(20000000)
input = sys.stdin.readline

FF, FS, SF, SS = map(int, input().split())
answer = 0
if FF == 0 and FS == 0:
    answer = SS
    if SF > 0:
        answer += 1
elif FS == 0:
    answer = FF
else:
    if FS > SF:
        answer = FF + SS + SF + SF + 1
    else:
        answer = FF + SS + FS + FS

print(answer)