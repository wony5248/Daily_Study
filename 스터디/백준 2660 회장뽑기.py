member = int(input())
rel =[[100 for _ in range(member+1)] for _ in range(member+1)]
visit = [[0 for _ in range(member+1)] for _ in range(member+1)]
hubo= []




while True:
    a, b = map(int, input().split())

    if a == -1 and b == -1:
        break
    else:
        rel[a][b] = 1
        rel[b][a] = 1

    for i in range(1, member+1):
        if rel[i] == min(rel):
            hubo.append(i)
print(rel)