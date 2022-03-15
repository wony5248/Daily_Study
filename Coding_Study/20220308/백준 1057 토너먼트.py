import sys
input = sys.stdin.readline
N, K, L = map(int, input().rstrip().split())
ans = 0

while K != L:
    K -= K // 2
    L -= L // 2
    ans += 1

print(ans)
