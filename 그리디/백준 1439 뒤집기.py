string = input()
reduce = [string[0]]
for i in range(1,len(string)):
    if string[i] != string[i-1]:
        reduce.append(string[i])
zcount = reduce.count("0")
ocount = reduce.count("1")
count = min(zcount, ocount)
print(count)