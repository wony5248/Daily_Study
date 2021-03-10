import sys
N, M = map(int, sys.stdin.readline().split())
listen =set(sys.stdin.readline().strip() for _ in range(N))
show = set(sys.stdin.readline().strip() for _ in range(M))
result = []


for i in listen:   # 듣지 못하는 사람중
    if i in show:  # 못보는 사람에도 있다면
        result.append(i)

print(len(result))
result.sort()
for j in result:
    print(j)
