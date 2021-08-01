import sys
input = sys.stdin.readline
N, M = map(int, input().split())
up = 1
down = 1
for i in range(1, M+1):
    up *= N-i + 1
    down *= i


print(up // down)