import sys
input = sys.stdin.readline
K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

low, high = 1, max(lines)

while low <= high:
    mid = (low + high) // 2
    count = 0
    for line in lines:
        count += line // mid
    if count >= N:
        low = mid + 1
    else:
        high = mid - 1

print(high)