import sys
input = sys.stdin.readline
N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
mint = 822400000000000 * 2 + 1
height = 0
for i in range(257):       # 1 ~ 256 까지 기준 높이를 바꿔가며 모든 경우 탐색
    low = 0
    high = 0
    for j in range(N):
        for k in range(M):
            if ground[j][k] < i:
                low += i - ground[j][k]         # 기준 높이보다 낮은 땅의 수
            else:                   
                high += ground[j][k] - i        # 기준 높이보다 높은 땅의 수

    if high + B < low:       # 가방에 있는 블록 수보다 놓아야 할 땅 수가 더 많을때 
        continue
    time = low + (high * 2)
    if time <= mint:
        mint = time
        height = i

print(mint, height)