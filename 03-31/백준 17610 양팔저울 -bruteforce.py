from itertools import combinations
import sys
input = sys.stdin.readline
count = 0
K = int(input())
chu = list(map(int, input().split()))
num = sum(chu)
result = set()
lst = list()
for i in range(1,K+1):
    lst = list(combinations(chu, i))
    for j in range(len(lst)):
        result.add(sum(lst[j]))
print(result)
for i in range(1, num+1):
    if i in result:
        continue
    for j in range(K):
        if chu[j] +i in chu:
            result.add(i)
            break

for i in range(1, num+1):
    if i not in result:
        count += 1
print(count)
print(result)
