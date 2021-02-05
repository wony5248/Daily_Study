N = int(input())
lst = list()

for i in range(N):
    w, h = map(int, input().split())
    lst.append([w, h])
for j in lst:
    grade = 1
    for k in lst:
        if j[0] < k[0] and j[1] < k[1]:
            grade += 1
    print(grade, end=" ")


