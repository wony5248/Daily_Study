import sys
size = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp = []
for i in range(size):
    for j in range(i+1, size):
        if A[i] < A[j]