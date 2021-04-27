N = int(input())
result = []
i = 666
while True:

    if "666" in str(i):
        result.append(i)
    i += 1
    if len(result) > N-1:
        break

print(result[N-1])