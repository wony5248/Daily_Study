N = int(input())
minV = 0
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
for i in range(len(A)):
    minV += A[i] * B[i]

print(minV)

