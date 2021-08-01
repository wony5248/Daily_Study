import sys
N, C = map(int, sys.stdin.readline().split())
house = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
house.sort()

minV = 1     # 최소 간격
maxV = house[-1] - house[0]    # 최대 간격


result = 0
while minV <= maxV:
    mid = (minV + maxV) // 2   # 와이파이 설치 간격
    count = 1  # 와이파이 갯수
    tmp = house[0]  # 이전 집
    for i in range(1, N):
        if house[i] >= tmp + mid:   # 설치 간격이 충족 된다면
            tmp = house[i]
            count += 1

    if count >= C:   # 와이 파이 다 설치 했으면 간격 넓힘
        minV = mid + 1
        result = mid
    else:            # 와이파이 갯수 부족하면 간격 좁힘
        maxV = mid -1

print(result)
# print(house)

