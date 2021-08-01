import sys
input = sys.stdin.readline
K = int(input())
stack = []
for i in range(K):
    x = int(input())
    if x == 0:
        stack.pop()
    else:
        stack.append(x)


if stack:
    print(sum(stack))
else:
    print(0)