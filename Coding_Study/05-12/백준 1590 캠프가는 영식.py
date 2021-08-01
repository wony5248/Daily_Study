import sys
input = sys.stdin.readline
N, T = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
minV = 2147483648


for j in range(N):
    bus = [0 for _ in range(lst[j][2])]
    bus[0] = lst[j][0]
    for i in range(1, lst[j][2]):
        bus[i] = bus[i-1] + lst[j][1]
    if max(bus) >= T:
        for k in bus:
            if k >= T and minV > k:
                minV = k

if minV >= T and minV != 2147483648:
    print(minV - T)
else:
    print(-1)
