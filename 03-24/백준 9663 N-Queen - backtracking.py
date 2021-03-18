
N = int(input())
graph = [0 for _ in range(N)]
leftup = [0 for _ in range(N*2 - 1)]
rightdown = [0 for _ in range(N*2 - 1)]
result = 0
time = 0
def dfs(count):
    global time
    time += 1
    global result
    if count == N:
        result += 1
        return
    for i in range(N):
       if graph[i] == 0 and leftup[count + i] == 0 and rightdown[count-i + N - 1] == 0:
           graph[i] = leftup[count + i] = rightdown[count - i + N - 1] = 1
           dfs(count + 1)
           graph[i] = leftup[count + i] = rightdown[count - i + N - 1] = 0

dfs(0)
print(result)
print(time)
