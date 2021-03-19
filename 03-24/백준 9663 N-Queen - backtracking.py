
N = int(input())
graph = [0 for _ in range(N)]                    # 세로
leftup = [0 for _ in range(N*2 - 1)]             # 왼쪽 아래에서 오른쪽 위로 가는 대각선
rightdown = [0 for _ in range(N*2 - 1)]          # 왼쪽 위에서 오른쪽 아래로 가는 대각선
result = 0

def dfs(count):
    global time
    global result
    if count == N:                               # 퀸을 N개 놓았다면 result +1 해주고 return
        result += 1
        return
    for i in range(N):
       if graph[i] == 0 and leftup[count + i] == 0 and rightdown[count-i + N - 1] == 0:
           graph[i] = leftup[count + i] = rightdown[count - i + N - 1] = 1
           dfs(count + 1)
           graph[i] = leftup[count + i] = rightdown[count - i + N - 1] = 0

dfs(0)
print(result)

