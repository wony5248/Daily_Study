import heapq
import sys
input = sys.stdin.readline                 # 이거 안하면 시간초과
N, H, T = map(int, input().split())
heap = []
count = 1
hammer = 0
for i in range(N):
    height = int(input())
    heapq.heappush(heap, (-1 * height))

while hammer < T:                        # 망치 쓴 횟수가 망치 기회보다 많으면 종료
    x = heapq.heappop(heap) * -1
    if x == 1:                           # 거인중 가장 큰애가 1 이면 종료
        heapq.heappush(heap, -x)
        break
    elif H == 1 and x != 1:              # 센티 키가 1이고 거인키가 1 이 아니면 거인 2 나눠줌
        x = x // 2
        hammer += 1
        heapq.heappush(heap, -x)
    elif 1 <= x < H:                     # 거인 키가 센티보다 작으면 
        heapq.heappush(heap, -x)
        break
    elif x >= H and x > 1:               # 거인이 센티보다 크거나 같고 1보다 크면
        x = x // 2
        hammer += 1
        heapq.heappush(heap, -x)
    else:
        hammer += 1
        heapq.heappush(heap, -x)
        break


result = heapq.heappop(heap) * -1


if result >= H:
    print("NO")
    print(result)

else:
    print("YES")
    print(hammer)