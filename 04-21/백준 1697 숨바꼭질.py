from collections import deque
MAX = 100001
subin, dongsang = map(int, input().split())
visit = [0] * MAX
queue = deque()
queue.append(subin)
while queue:
    x = queue.popleft()
    if x == dongsang:
        print(visit[x])
        break
    for i in (x-1, x+1, x*2):              # -1 +1 *2 중에 이동
        if 0 <= i < MAX and not visit[i]:         # 최소기때문에 한번 방문시 재방문 필요 X
            visit[i] = visit[x]+1
            queue.append(i)
