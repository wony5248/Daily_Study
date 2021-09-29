import sys

result = 0


def z(n, x, y):
    global result
    if n == 1:
        visit[x][y] = result
        result += 1
        return

    z(n // 2, x, y)
    z(n // 2, x, y + n // 2)
    z(n // 2, x + n // 2, y + n // 2)
    z(n // 2, x + n // 2, y)



n, r, c = map(int, sys.stdin.readline().split(' '))
visit = [[0 for _ in range(2**n)] for _ in range(2**n)]
z(2 ** n, 0, 0)
for i in range(2 ** n):
    print(visit[i])