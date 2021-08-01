A, B = input().split()
B = list(B)

maxV = 0
while len(A) <= len(B):
    cnt = 0
    for i in range(len(A)):
        if A[i] == B[i]:
            cnt += 1
        maxV = max(maxV, cnt)
    del B[0]
print(len(A) - maxV)