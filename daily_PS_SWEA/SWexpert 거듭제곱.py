
def squre(n, m, s):
    s = s * n
    if m == 2:
        return s
    return squre(n, m-1, s)

for i in range(10):
    TC = int(input())
    N, M = map(int, input().split())
    print("#%d %d" %(TC, squre(N,M,N)))