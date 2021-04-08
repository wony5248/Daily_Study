N, M = map(int, input().split())
lad = []
snake = []
x = 1
count = 0
for i in range(N):
    x, y = map(int, input().split())
    lad.append([x, y])
for i in range(M):
    x, y = map(int, input().split())
    snake.append([x, y])
while True:
    for i in range(len(lad)):
        if x
lad.sort(key= lambda x : (-(x[1] - x[0]), x[0]))
print(lad)
print(snake)