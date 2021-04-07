result = []
for i in range(10000):
    tmp = 0
    string = str(i)
    tmp += i
    for j in range(len(string)):
        tmp += int(string[j])
    result.append(tmp)
for j in range(10000):
    if j not in result:
        print(j)

