import sys


input = sys.stdin.readline
N, K = map(int, input().split())
stack = []
num = list(map(int, input().rstrip()))
cnt = 0
result = ""
for i in range(N):
    while cnt < K and stack:
        if stack[-1] < num[i]:
            stack.pop()
            cnt += 1
        else:
            break
    stack.append(num[i])

for i in range(N-K):
    print(stack[i], end="")


