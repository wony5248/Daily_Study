n = int(input())
m = int(input())
lst = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    lst[a][b] = c



print(lst)