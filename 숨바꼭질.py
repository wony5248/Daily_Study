from collections import deque
MAX = 100001
subin, dongsang = map(int, input().split())
seconds = [0] * MAX
queue = deque()
queue.append(subin)
while queue:
    x = queue.popleft()
    if x == dongsang:
        print(seconds[x])
        break
    for i in (x-1, x+1, x*2):
        if 0 <= i < MAX and not seconds[i]:
            seconds[i] = seconds[x]+1
            queue.append(i)
