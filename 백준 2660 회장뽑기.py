member = int(input())
rel =[[] for _ in range(member+1)]
visit = [0 for _ in range(member+1)]

while True:
    a, b = map(int, input().split())

    if a == -1 and b == -1:
        break
    else:
        rel[a].append(b)

print(rel)