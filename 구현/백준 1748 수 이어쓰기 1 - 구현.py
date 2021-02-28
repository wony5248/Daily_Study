N = input()
length = len(N)
result = 0
i = 0
while i < length - 1:
    result += 9 * (10 ** i) * (i + 1)
    i += 1
result += ((int(N) - (10 ** (length - 1))) + 1) * length
print(result)