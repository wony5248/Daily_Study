N = int(input())
lst = [[] for _ in range(N)]
for i in range(N):
    start, end = map(int, input().split())
    lst[i] = [start, end]

lst.sort(key= lambda x:(x[1],x[0]))

result = 0
check = 0
for x, y in lst:
    if x >= check:
        check = y
        result += 1
print(result)