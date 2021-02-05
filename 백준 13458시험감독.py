import sys
import math
N = int(input())
A = list(map(int, sys.stdin.readline().split()))

B, C = map(int, sys.stdin.readline().split())
count = [0 for _ in range(N)]
for i in range(N):
    A[i] = A[i] - B
    count[i] = count[i] +1
    if A[i] > 0:
        count[i] = count[i] + math.ceil(A[i]/ C)



print(sum(count))
