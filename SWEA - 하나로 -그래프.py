T = int(input())

for i in range(T):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())

    result = 0
    count = 0
    INF = float("inf")
    weight = [INF for _ in range(N)]
    distance = [[0 for _ in range(N)] for _ in range(N)]
    visit = [0 for _ in range(N)]

    for j in range(N):
        for k in range(N):
            distance[j][k] = ((x[k] - x[j]) ** 2 + (y[k] - y[j]) ** 2)
            distance[k][j] = ((x[k] - x[j]) ** 2 + (y[k] - y[j]) ** 2)


    weight[0] = 0
    while count < N:                 # MST가 아닐 조건 - 최소 간선은 정점 -1
        minV = INF                      
        u = -1
        for j in range(N):
            if visit[j] == 0 and weight[j] < minV:
                minV = weight[j]
                u = j

        visit[u] = 1
        result += minV
        count +=1

        for w in range(N):
            if distance[u][w] > 0 and visit[w] == 0 and weight[w] > distance[u][w]:
                weight[w] = distance[u][w]



    print("#%d %d" %(i+1, round(result * E)))
