number = int(input())
student = list(map(int, input().split()))
result = []
for i in range(number):
    result.append(i+1)
for i in range(1, number):
    result.insert(i-student[i], i+1)
result = result[0:number]
# for i in range(number):
#     print(result[i], end=" ")

print(result)