from itertools import combinations
T = int(input())
for i in range(T):
    K = int(input())
    string = list(input())
    length = len(string)
    result = []
    count = 0
    for j in range(length+1):
        for k in range(j+1, length+1):
            final = "".join(string[j:k])
            result.append(final)
    result = list(set(result))
    result.sort()

    count = len(result)

    if K > count:
        print("#%d none" %(i + 1))
    else:
        print("#%d %s" %(i + 1, result[K-1]))