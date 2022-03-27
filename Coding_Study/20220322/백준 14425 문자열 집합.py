import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
S = [input().rstrip() for _ in range(N)]
S = set(S)
G = [input().rstrip() for _ in range(M)]
cnt = 0
for i in G:
    if i in S:
        cnt += 1

print(cnt)