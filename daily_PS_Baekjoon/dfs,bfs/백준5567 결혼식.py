n = int(input())
m = int(input())
friends = [[0 for i in range(n)] for j in range(n)]
record = [0 for i in range(n)]
final = set()
for i in range(m):
    rel = list(map(int, input().split()))
    if rel[0] == 1:
        record.append(rel[1]-1)
        final.add(rel[1]-1)
    friends[rel[0]-1][rel[1]-1] = 1
    friends[rel[1]-1][rel[0]-1] = 1
while record:
    num = record.pop()
    for i in range(1,n):
        if friends[num][i] ==1:
            final.add(i)

print(len(final))




