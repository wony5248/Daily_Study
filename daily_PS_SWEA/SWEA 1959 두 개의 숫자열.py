T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = []



    for j in range(max(N,M) - min(N, M) + 1):
        count = 0
        for k in range(j, j+min(N, M)):
            count += A[k] * B[k]
        result.append(count)
        if len(A) < len(B):
            A.insert(0, 0)
        elif len(A) > len(B):
            B.insert(0, 0)

    print("#%d %d" % (i+1, max(result)))

