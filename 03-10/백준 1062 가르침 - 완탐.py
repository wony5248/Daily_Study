import sys
from itertools import combinations
from string import ascii_lowercase
N, K = map(int, sys.stdin.readline().split())
string = set()
for _ in range(N):
    string.add(set(sys.stdin.readline().rstrip()[4:-4]).difference("a", "c", "i", "t", "n"))
tmp = set(ascii_lowercase).difference("a", "c", "i", "t", "n")
result = 0
if K < 5:
    result = 0
elif K == 26:
    result = N
else:
    for i in set(combinations(tmp, K-5)):
        count = 0
        for j in string:
            if not j.difference(i):
                count += 1

        result = max(result, count)
# 97~122

print(result)