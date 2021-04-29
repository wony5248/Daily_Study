import sys
from collections import deque
input = sys.stdin.readline

T = int(input().rstrip())
for i in range(T):
    K = int(input().rstrip())
    queue = deque()
    for j in range(K):
        com = input().rstrip().split()
        if com[0] == "I":
            queue.append(int(com[1]))
        elif com[0] == "D" and queue:
            queue = deque(sorted(list(queue)))
            if com[1] == "-1":
                queue.popleft()
            elif com[1] == "1":
                queue.pop()
        elif com[0] == "D" and not queue:
            continue

    if not queue:
        print("EMPTY")
    else:
        print("%d %d" %(max(queue), min(queue)))



