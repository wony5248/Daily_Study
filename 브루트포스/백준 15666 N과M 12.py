from itertools import combinations_with_replacement
N, M = map(int, input().split())
result = list(map(int,input().split()))
result.sort()
lst = list(set(combinations_with_replacement(result,  M)))
lst.sort()
for i in lst:
    print(*i)