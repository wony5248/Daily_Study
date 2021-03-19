import heapq
T = int(input())
for _ in range(T):
    N = int(input())
    result = 0
    answer = [0 for _ in range(N)]
    L = list(map(int, input().split()))
    length = len(L)
    heapq.heapify(L)                        # 가장 작은값 두개씩 뽑아서 새 배열에 양끝부터 넣어줌 0, n-1 -> 1, n-2 -> 2, n-3
    if length % 2 == 1:                     # 통나무 개수 홀수면은 마지막에 한개만 남음
        for i in range(length//2 + 1):
            if len(L) > 1:
                answer[i] = heapq.heappop(L)
                answer[N-1-i] = heapq.heappop(L)
            else:                           # 남은 한개의수 가운데에 넣어줌
                answer[N//2] = heapq.heappop(L)
    else:                                   # 통나무 개수 짝수면은 딱 떨어짐
        for i in range(length//2):
            answer[i] = heapq.heappop(L)
            answer[N-1-i] = heapq.heappop(L)
    for i in range(1, len(answer)):         # 새로 만들어진 배열 탐색 하면서 양 옆 나무와의 높이 차이 최대값 찾아냄
        if abs(answer[i] - answer[i-1]) > result:
            result = abs(answer[i] - answer[i-1])
        if result < abs(answer[-1] - answer[0]):
            result = abs(answer[-1] - answer[0])

    print(result)