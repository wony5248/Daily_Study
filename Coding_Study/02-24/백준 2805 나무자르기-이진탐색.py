# pypy3 제출

import sys
N, M = map(int, sys.stdin.readline().split())
height = list(map(int, sys.stdin.readline().split()))

maxheight = max(height)                  # 나무중 가장 높은 나무와
minheight = 0                       # 나올수 있는 나무의 최솟 값
result = 0
while True:
    if minheight > maxheight:     # 나무의 최솟 값이 최댓 값보다 커지면 종료
        break
    avg = (maxheight + minheight) // 2        # 기준을 계속 나무의 최대와 최소의 평균으로 해준다
    total = 0
    for i in range(N):
        if avg < height[i]:                   # 기준보다 큰 나무들을 기준으로 나무-기준을 total에 넣어줌
            total += height[i] - avg
    if total >= M:                            # total 이 필요한 나무보다 크면 result에 평균을 넣어줌
        result = avg                          # 지금 기준으로 필요한 나무 충족 - 최대 높이인지는 모름 -> min을 avg + 1로
        minheight = avg + 1
    elif total < M:                           # 지금 기준으로 나무가  부족하니 높이를 낮춰줌 -> max를 avg -1로
        maxheight = avg - 1

print(result)


# import sys
# n,m = map(int, sys.stdin.readline().split())
# trees = list(map(int, sys.stdin.readline().split()))
# low = 0
# high = max(trees)
# k = (low + high) / 2
# FindHeight = False
# while not FindHeight:
#     s = 0
#     for i in trees:
#         if i - k >= 0:
#             s += (i-k)
#     if s < m:
#         high = k
#         k = (low + k) /2
#     if s > m:
#         low = k
#         k = (high + k) /2
#     if s==m:
#         FindHeight = True
#         Result = k
# print(Result)


