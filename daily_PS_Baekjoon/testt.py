from itertools import combinations
n = int(input())
for i in range(n // 2 + 1):
    lst = [st for st in combinations(range(1, n+1), i)]
    print(lst)