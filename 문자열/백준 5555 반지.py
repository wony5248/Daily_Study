import sys
input = sys.stdin.readline
search = input().rstrip()
N = int(input())
ring = list(input().rstrip() for _ in range(N))
result = 0
for i in range(N):
    ring[i] += ring[i]
    if ring[i].count(search):
        result += 1


print(result)