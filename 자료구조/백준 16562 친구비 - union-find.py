import sys
sys.setrecursionlimit(500000)
N, M, K = map(int, sys.stdin.readline().split())
cost =  [0] + list(map(int, sys.stdin.readline().split()))



parent = [0 for i in range(N + 1)]
isflag =0
lst = []
result = [[] for _ in range(N+1)]
answer = 0
def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    lst.append([x, y])
    parent[x] = x
    parent[y] = y

for i in range(M):
    union(lst[i][0], lst[i][1])
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == find(parent[j]):
            result[i].append(j)
for i in range(len(result)):
    tmp = 0
    if result[i]:
        tmp = 10000000
        for j in range(len(result[i])):
            if cost[result[i][j]] < tmp:
                tmp = cost[result[i][j]]
    answer += tmp
for i in range(1, len(parent)):
    if parent[i] == 0:
        if answer + cost[i] <= K:
            answer += cost[i]
            parent[i] = i

if parent.count(0) > 1 or answer > K:
    print("Oh no")

else:
    print(answer)




