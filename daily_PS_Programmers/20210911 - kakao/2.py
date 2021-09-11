from math import sqrt


def change(n, k):
    base = ""
    while n > 0:
        n, mod = divmod(n, k)
        base += str(mod)
    return base[::-1]


def solution(n, k):
    answer = 0
    lst = []
    primelst = []
    result = change(n, k)
    str = ""
    for i in range(len(result)):
        if i == len(result) - 1:
            if result[i] != "0":
                str += result[i]
            if str != "1" and str != "":
                lst.append(str)
        elif result[i] != "0":
            str += result[i]
        elif result[i] == "0":
            if str != "1" and str != "":
                lst.append(str)
            str = ""
    for i in lst:
        isprime = 1
        if i.isdecimal():
            for j in range(2, int(sqrt(int(i))) + 1):
                if int(i) % j == 0:
                    isprime = 0
            if isprime == 1:
                primelst.append(i)
    print(result)
    print(lst)
    answer = len(primelst)
    return answer