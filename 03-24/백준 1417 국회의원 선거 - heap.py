# import sys         # 시간 초과
# input = sys.stdin.readline
# count = 0
# N = int(input())
# cand = [int(input()) for _ in range(N)]
# isflag = 1
# while isflag:
#     for i in range(1, N):
#         if cand[i] == max(cand) and cand[i] >= cand[0]:
#             cand[i] -= 1
#             cand[0] += 1
#             count += 1
#         if cand[0] == max(cand) and cand.count(max(cand)) == 1:
#             isflag = 0
#             break
#
# print(count)


import heapq
import sys
input = sys.stdin.readline

N = int(input())
cand = []
count = 0
dasom = 0
isflag = 1
for i in range(N):          # 후보자 빼고 다 heapq에 넣어줌  -> 음수 취해서 넣어줌 = 최대힙
    x = int(input())
    if i == 0:             
        dasom = x
    else:
        heapq.heappush(cand, -x)

while isflag:
    if not cand:     # 후보자가 다솜이만 있을 경우 -> 종료
        break
    y = (heapq.heappop(cand) * -1)       # 후보자중 표수 제일 많은 사람 빼줌

    if y >= dasom:              # 그사람이 다솜이보다 표수 같거나 많다면
        y -= 1                  # 그 사람 표수 1 빼주고 다솜이 한표주고 count 1 증가
        heapq.heappush(cand, -y)
        dasom += 1
        count += 1
    else:                      # 다솜제외 표 젤 많은 사람이 다솜이보다 표 적다면
        heapq.heappush(cand, -y)
        isflag = 0            # 종료

print(count)
