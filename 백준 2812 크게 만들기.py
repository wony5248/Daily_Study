from itertools import permutations
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
result = 0
num = list(input())
x = list(permutations(num, N-K))
cop = ["" for _ in range(len(x))]
for i in range(len(x)):
    cop[i] = "".join(x[i])
    if int(cop[i]) > result:
        result = int(cop[i])
print(result)