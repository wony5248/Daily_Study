# import sys
# from collections import deque
# input = sys.stdin.readline
#
# T = int(input().rstrip())
# for i in range(T):
#     K = int(input().rstrip())
#     queue = deque()
#     for j in range(K):
#         com = input().rstrip().split()
#         if com[0] == "I":
#             queue.append(int(com[1]))
#         elif com[0] == "D" and queue:
#             queue = deque(sorted(list(queue)))
#             if com[1] == "-1":
#                 queue.popleft()
#             elif com[1] == "1":
#                 queue.pop()
#         elif com[0] == "D" and not queue:
#             continue
#
#     if not queue:
#         print("EMPTY")
#     else:
#         print("%d %d" %(max(queue), min(queue)))



import sys
import heapq
input = sys.stdin.readline


test = int(input())
for _ in range(test):
    max_heap, min_heap = [], []
    visit = [False] * 1000001

    order_num = int(input())

    for key in range(order_num):
        order = input().rsplit()
        if order[0] == 'I':
            heapq.heappush(min_heap, (int(order[1]), key))
            heapq.heappush(max_heap, (int(order[1]) * -1, key))
            visit[key] = True #True이면 어떤 힙에서도 아직 삭제되지 않은 상태

        elif order[0] == 'D':
            if order[1] == '-1': #삭제연산시, key값을 기준으로 해당 노드가 다른힙에서 삭제된 노드인가를 먼저 판단한다.
                # 이미 상대힙에 의해 삭제된 노드인경우 삭제되지 않은 노드가 나올때까지 계쏙 버리다가 이후 삭제대상노드가 나오면 삭제한다.
                while min_heap and not visit[min_heap[0][1]]: # visit이 False일떄 -> 해당노드가 삭제된상태
                    heapq.heappop(min_heap) # 버림 (상대힙에서 이미 삭제된노드이므로)
                if min_heap:
                    visit[min_heap[0][1]] = False # visit이 Ture엿으므로 False로 바꾸고 내가 삭제함
                    heapq.heappop(min_heap)
            elif order[1] == '1':
                while max_heap and not visit[max_heap[0][1]]: #이미 삭제된 노드인경우 삭제되지 않은 노드가 나올때까지 모두 버린다.
                    heapq.heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

# 모든 연산이 끝난후에도 쓰레기 노드가 들어있을수 있으므로, 결과를 내기전 모두 비우고 각 힙의 첫번째 원소값을 출력한다.
    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')