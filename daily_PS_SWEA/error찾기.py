n = int(input())
move_list = [(0, -1), (0, 1), (-1, 0), (1, 0)]
h_map = [list(map(int, input())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
count_list = []
q = []

for i in range(n):
    for j in range(n):
        if not visited[i][j] and h_map[i][j]:
            visited[i][j] = 1
            q.append((i,j))
            count = 0
            while (len(q)):
                i, j = q.pop(0)
                count += 1
                for x, y in move_list:
                    if 0 <= i+y < n and 0 <= j+x < n:
                        if not visited[i+y][j+x] and h_map[i+y][j+x]:
                            visited[i+y][j+x] = 1
                            q.append((i+y, j+x))
            count_list.append(count)
print(len(count_list))
count_list.sort()
for count in count_list:
    print(count)