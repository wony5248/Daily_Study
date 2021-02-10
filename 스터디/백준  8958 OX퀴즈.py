
TC = int(input())
result = [0 for _ in range(TC)]
lst = []

for i in range(TC):
    count = 0
    lst.append(list(input()))
    for j in range(len(lst[i])):
        if lst[i][j] == "O":
            count += 1
            result[i] += count
        elif lst[i][j] == "X":
            count = 0
for i in range(TC):
    print(result[i])
