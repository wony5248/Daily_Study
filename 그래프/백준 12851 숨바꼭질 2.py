from collections import deque
MAX = 100001
subin, dongsang = map(int, input().split())
visit = [-1] * MAX
queue = deque()
count = 0
queue.append(subin)
visit[subin] = 0
while queue:
    x = queue.popleft()
    if x == dongsang:
        count += 1
    for i in (x * 2, x-1, x+1):              # -1 +1 *2 중에 이동
        if 0 <= i < MAX and (visit[i] == -1 or visit[i] >= visit[x] + 1):         # 최소기때문에 한번 방문시 재방문 필요 X
            visit[i] = visit[x]+1
            queue.append(i)

print(visit[dongsang])
print(count)
