N = int(input())
num = 0
for i in range(N):
    count = 0
    str1 = input()
    for j in range(1, len(str1)):
        if str1[j] != str1[j - 1]:
            newstr = str1[j:]
            if newstr.find(str1[j - 1]) != -1:
                count += 1
    if count == 0:
        num += 1
print(num)