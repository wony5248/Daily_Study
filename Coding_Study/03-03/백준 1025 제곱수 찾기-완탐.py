import math
n, m = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int,list(input()))))

res = -1
for i in range(n):
    for j in range(m):
        for k in range(-n,n):
            for s in range(-m,m):
                if k == 0 and s == 0:
                    continue
                x, y = j, i
                num = 0
                while x>=0 and x<m and y>=0 and y<n:
                    num *= 10
                    num += board[y][x]
                    if num == int(math.sqrt(num))*int(math.sqrt(num)) and res < num:
                        res = num
                    x += s
                    y += k

print(res)