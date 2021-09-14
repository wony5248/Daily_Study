import sys
input = sys.stdin.readline
N = int(input())

dp1 = [0 for _ in range(3)]
dp2 = [0 for _ in range(3)]
dp3 = [0 for _ in range(3)]
dp4 = [0 for _ in range(3)]
dp5 = [0 for _ in range(3)]
dp6 = [0 for _ in range(3)]

maxV = 0
minV = 0
stair1 = list(map(int, input().split()))
dp1[0], dp2[0], dp3[0] = stair1[0], stair1[1], stair1[2]
dp4[0], dp5[0], dp6[0] = stair1[0], stair1[1], stair1[2]
for i in range(1, N):

    stair = list(map(int, input().split()))
    dp1[i % 3] = max(dp1[(i-1) % 3] + stair[0], dp2[(i-1) % 3] + stair[0])
    dp2[i % 3] = max(dp1[(i-1) % 3] + stair[1], dp2[(i-1) % 3] + stair[1], dp3[(i-1) % 3] + stair[1])
    dp3[i % 3] = max(dp2[(i-1) % 3] + stair[2], dp3[(i-1) % 3] + stair[2])
    dp4[i % 3] = min(dp4[(i-1) % 3] + stair[0], dp5[(i-1) % 3] + stair[0])
    dp5[i % 3] = min(dp4[(i-1) % 3] + stair[1], dp5[(i-1) % 3] + stair[1], dp6[(i-1) % 3] + stair[1])
    dp6[i % 3] = min(dp5[(i-1) % 3] + stair[2], dp6[(i-1) % 3] + stair[2])

maxV = max(dp1[(N-1) % 3], dp2[(N-1) % 3], dp3[(N-1) % 3])
minV = min(dp4[(N-1) % 3], dp5[(N-1) % 3], dp6[(N-1) % 3])

print(maxV, minV)

