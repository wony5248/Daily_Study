import sys
input = sys.stdin.readline
K, N = map(int, input().rstrip().split())
lan = [int(input().rstrip()) for _ in range(K)]
low = 1
high = max(lan)
while low <= high:
    mid = (low + high) // 2
    cnt = 0
    for l in lan:
        cnt += l // mid
    if cnt >= N:
        low = mid + 1
    else:
        high = mid - 1
print(high)
