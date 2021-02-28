import sys
N, M = map(int, sys.stdin.readline().split())
listen =[sys.stdin.readline().strip() for i in range(N)]
show = [sys.stdin.readline().strip() for i in range(M)]


result = list(set(listen) & set(show))

print(len(result))
result.sort()
for j in result:
    print(j)
