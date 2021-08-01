import sys
from collections import deque

lst = []
while True:
    word = input().rstrip()
    if word == "-":
        break
    lst.append(word)
print(lst)
while True:
    fword = input().rstrip()
    if fword == "#":
        break
    else:
        dic = dict()
        for fw in fword:
            if fw not in dic.keys():
                dic[fw] = 1
            else:
                dic[fw] += 1
print(dic)