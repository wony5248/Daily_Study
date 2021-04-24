import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lst = list(map(int, input().split()))

count = 0
for i in range(len(lst)):
    tmp = 0
    for j in range(i, len(lst)):
        tmp += lst[j]
        if tmp == M:
            count += 1
            break
        elif tmp > M:
            break

print(count)