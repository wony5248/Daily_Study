import heapq
N = int(input())
k = int(input())
B = []
result = 0
high = k
low = 0

while low <= high:
    mid = (low + high) // 2
    cnt = 0
    for i in range(1, N+1):
        cnt += min(mid//i, N)

    if cnt < k:
        low = mid + 1
    else:
        result = mid
        high = mid - 1

print(result)