N = int(input())
A = list(map(int, input().split()))
A.sort()
answer = 0
if N % 2 == 0:
    answer = A[0] * A[-1]
else:
    answer = A[N//2] ** 2

print(answer)