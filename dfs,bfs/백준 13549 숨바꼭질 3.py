from collections import deque
MAX = 100001
subin, dongsang = map(int, input().split())
seconds = [0] * MAX
visit = [0] * MAX
queue = deque()
queue.append(subin)
while queue:
    x = queue.popleft()
    if x == dongsang:
        print(seconds[x])
        break
    for i in (x*2, x-1, x+1):
        if 0 <= i < MAX and not visit[i]:
            if i == x*2:
                seconds[i] = seconds[x]
                visit[i] = 1
                queue.append(i)
            else:
                seconds[i] = seconds[x]+1
                visit[i] = 1
                queue.append(i)
