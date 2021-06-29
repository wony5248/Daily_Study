from itertools import permutations
import sys
input = sys.stdin.readline
name = list(input().rstrip())
palin = list(set(permutations(name, len(name))))
result = []
for i in range(len(palin)):
    palin[i] = list(palin[i])
    if len(palin[i]) % 2 == 0:
        if palin[i][:(len(palin[i])//2)] == palin[i][(len(palin[i])//2):][::-1]:
            result.append("".join(palin[i]))
    else:
        if palin[i][:(len(palin[i])//2)] == palin[i][(len(palin[i])//2) - 1:][::-1]:
            result.append("".join(palin[i]))

result.sort()
if result:
    print(result[0])
else:
    print("I'm Sorry Hansoo")