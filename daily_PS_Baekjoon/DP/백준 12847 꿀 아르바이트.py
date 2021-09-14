import sys
input = sys.stdin.readline
n, m = map(int, input().split())
T = list(map(int, input().split()))
maxv = 0
for i in range(1, n):
    T[i] += T[i-1]
for j in range(m, n):
    if maxv < T[j] - T[j-m]:
        maxv = T[j] - T[j-m]
print(max(maxv, T[m-1]))

