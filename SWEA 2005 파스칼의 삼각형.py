T = int(input())

for i in range(T):
    N = int(input())
    graph = [[] for _ in range(N)]
    for j in range(1, N+1):
        for k in range(j):
            if j >= 3 and 0 < k < j-1:
                graph[j - 1].append(graph[j-2][k-1] + graph[j-2][k])
            else:
                graph[j - 1].append(1)
    print("#%d" %(i+1))
    for j in range(1, N+1):
        for k in range(j):
            print(graph[j-1][k], end=" ")
        print()

