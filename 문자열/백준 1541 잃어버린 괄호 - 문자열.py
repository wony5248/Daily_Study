exp = list(input().split("-"))
result = []

for i in exp:
    count = 0
    inner = i.split("+")
    print("1", end= " ")
    print(i)
    print("2", end=" ")
    print(inner)
    for j in inner:
        count += int(j)
        print(count)
    result.append(count)
n = result[0]
for i in range(1, len(result)):
    n -= result[i]
print(n)


print(exp)

