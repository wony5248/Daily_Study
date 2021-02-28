from collections import deque
count = 0
str1 = input()
str2 = input()

compare = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i-1] == str2[j-1]:
            compare[i][j] = compare[i-1][j-1] + 1
        else:
            compare[i][j] = max(compare[i][j-1], compare[i-1][j])
print(compare[len(str1)][len(str2)])
