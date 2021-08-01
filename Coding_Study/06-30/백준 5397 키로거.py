from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    L = input().rstrip()
    left = deque()
    right = deque()
    for j in L:
        if j == "<":
            if len(left) != 0:
                right.appendleft(left.pop())
        elif j == ">":
            if len(right) != 0:
                left.append(right.popleft())
        elif j == "-":
            if len(left) != 0:
                left.pop()
        else:
            left.append(j)

    print("".join(left + right))






