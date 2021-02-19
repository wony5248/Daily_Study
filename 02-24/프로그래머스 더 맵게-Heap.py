import heapq             # 리스트를 자동으로 정렬해주고 삽입시 정렬순으로 삽입해줌

s = list(map(int, input().split()))
hot = int(input())
def solution(scoville, K):
    answer = 0
    heap = heapq.heapify(scoville)               # scoville 배열을 heapq로 만들어줌
    while scoville[0] < K:
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)     #scoville 배열에 가장 낮은 지수의 scoville 두개 빼주고 섞은값 추가

        if len(scoville) == 1 and scoville[0] < K:         #스코빌레가 하나 남았고 하나가 K보다 작을때
            answer = -1
            break
        answer += 1

    return answer
print(solution(s, hot))