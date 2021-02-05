num = list(map(int, input().split()))
num.sort()
final= num[0] * 1000 + num[1] * 100 + num[2] * 10 + num[3]
print(final)