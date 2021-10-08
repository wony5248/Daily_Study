from collections import Counter


def solution(str1, str2):
    answer = 0
    result = 0
    lst1 = list()
    lst2 = list()
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            lst1.append((str1[i] + str1[i + 1]).lower())
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            lst2.append((str2[i] + str2[i + 1]).lower())

    Counter1 = Counter(lst1)
    Counter2 = Counter(lst2)

    sumV = list((Counter1 | Counter2).elements())
    subV = list((Counter1 & Counter2).elements())
    if len(sumV) == 0:
        result = 1
    else:
        result = len(subV) / len(sumV)
    answer = int(65536 * result)
    return answer