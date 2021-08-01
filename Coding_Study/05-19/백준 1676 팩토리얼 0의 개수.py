N = int(input())
result = 0
for i in range(1, N+1):            # ! 0의 갯수는 10의 개수 즉 2의 배수와 5의 배수중 작은게 답
    if i % 5 == 0:
        result += 1
    if i % 25 == 0:                # 25 의배수는 5  2개들어가기에 +1
        result += 1
    if i % 125 == 0:               # 125읩 배수는 5 3개 + 1
        result += 1

print(result)



