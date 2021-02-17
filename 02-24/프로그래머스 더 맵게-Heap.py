import heapq

s = list(map(int, input().split()))
hot = int(input())
def solution(scoville, K):
    answer = 0
    heap = heapq.heapify(scoville)
    while scoville[0] < K:
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)

        if len(scoville) == 1 and scoville[0] < K:
            answer = -1
            break
        answer += 1

    return answer
print(solution(s, hot))