N = int(input())
dist = list(map(int, input().split()))
gas = list(map(int, input().split()))
result = 0
minV = gas[0]
for i in range(len(dist)):
    if gas[i] <= minV:
        minV = gas[i]
    result += minV * dist[i]



print(result)