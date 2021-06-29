from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
queue = deque()
for i in range(N):
    com = list(input().rstrip().split())
    if com[0] == "push_back":
        queue.append(int(com[1]))
    elif com[0] == "push_front":
        queue.appendleft(int(com[1]))
    elif com[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif com[0]== "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif com[0] == "size":
        print(len(queue))
    elif com[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif com[0] == "pop_front":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif com[0] == "pop_back":
        if queue:
            print(queue.pop())
        else:
            print(-1)