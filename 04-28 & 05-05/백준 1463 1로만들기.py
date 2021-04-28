N = int(input())

result = [0 for _ in range(1000001)]

for i in range(2, N+1):
    result[i] = result[i-1] + 1
    if i % 2 == 0:
        result[i] = min(result[i], result[i//2] + 1)
    if i % 3 == 0:
        result[i] = min(result[i], result[i//3] + 1)

print(result[N])