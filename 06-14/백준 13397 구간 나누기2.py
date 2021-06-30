import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().rstrip().split()))


def solve(cnt):
    maxV = minV = arr[0]
    count = 1
    for i in range(1, N):
        maxV = max(maxV, arr[i])
        minV = min(minV, arr[i])
        if maxV - minV > cnt:
            count += 1
            maxV = arr[i]
            minV = arr[i]
    return count


low, high = 0, max(arr)
result = 0
while low <= high:
    mid = (low + high) // 2
    if solve(mid) <= M:
        high = mid - 1
        result = mid
    else:
        low = mid + 1
print(result)