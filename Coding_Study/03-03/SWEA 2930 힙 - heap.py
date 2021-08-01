import heapq
T = int(input())

for i in range(T):
    tree = []
    N = int(input())
    result = []
    for j in range(N):
        x = list(map(int, input().split()))
        if x[0] == 1:                      # 연산 1이라면
            heapq.heappush(tree,-x[1])     # heapq에 넣는값의 음수를 취하여 넣어줌   -> 기존의 최댓값이 최솟값이 됨 
        elif x[0] == 2 and tree:           # 연산2 라면 heapq의 최솟값 빼고 * -1해서 result에 넣어줌   -> 최대값이 들어감
            result.append((heapq.heappop(tree)) * -1)
        elif x[0] == 2 and not tree:       # 연산2인데 heapq가 비었다면 result에 -1 넣어줌
            result.append(-1)
    print("#%d" %(i+1), end=" ")
    for j in range(len(result)):
        print(result[j], end=" ")
    print()


