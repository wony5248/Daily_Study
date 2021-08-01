import sys
input = sys.stdin.readline
poly = list(input().rstrip().split("-"))
final = []
for i in poly:
    result = 0
    poly2 = i.split("+")
    for j in poly2:
        result += int(j)
    final.append(result)

answer = final[0]

for i in range(1, len(final)):
    answer -= final[i]
print(answer)