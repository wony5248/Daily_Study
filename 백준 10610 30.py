from itertools import permutations
N = input()
lst = list(set(permutations(N, len(N))))
result = []
for i in range(len(lst)):
    if int("".join(lst[i])) % 30 == 0:
        result.append(int("".join(lst[i])))
if result:
    print(max(result))
else:
    print(-1)