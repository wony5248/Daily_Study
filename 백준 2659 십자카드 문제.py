num = list(map(int, input().split()))
num.sort()
th = num[0]
hd = num[1]
ten = num[2]
one = num[3]
com1 = num[2] % 9
com2 = num[3] % 9
result = com1 * (9 - com1) + com2 * (9 - com2)


print(result)