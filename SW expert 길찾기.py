from collections import deque

for i in range(10):
    stack = deque()
    graph = [[0 for _ in range(100)] for _ in range(100)]
    rel = [[0 for _ in range(100)] for _ in range(100)]
    visit = [0 for _ in range(100)]
    TC, length = map(int, input().split())
    x = list(map(int, input().split()))
    for j in range(0, length*2, 2):
        rel[x[j]].append(x[j+1])
    stack.append(0)
    visit[0] = 1
    result = 0
    while stack:
        x = stack.pop()
        for k in rel[x]:
            if k == 99:
                result = 1
                break
            if visit[k] == 0:
                stack.append(k)
                visit[k] = 1
    print("#%d %d"%(TC, result))













