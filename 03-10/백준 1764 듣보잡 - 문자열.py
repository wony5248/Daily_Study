import sys
N, M = map(int, sys.stdin.readline().split())
listen =set(sys.stdin.readline().strip() for i in range(N))
show = set(sys.stdin.readline().strip() for i in range(M))
result = []
if len(listen) >= len(show):
    for i in show:
        if i in listen:
            result.append(i)
else:
    for i in listen:
        if i in show:
            result.append(i)

print(len(result))
result.sort()
for j in result:
    print(j)
