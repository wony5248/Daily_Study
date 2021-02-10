N, M = map(int, input().split())
minf = 0
package = [0 for _ in range(M)]
one = [0 for _ in range(M)]
for i in range(M):
    package[i], one[i] = list(map(int, input().split()))
package.sort()
one.sort()
while True:
    if N <= 0:
        break
    elif N >= 6:
        minx = min(package[0], one[0] * 6)
        minf += minx
        N -= 6
    else:
        minv = min(package[0], one[0] * N)
        minf += minv
        N = 0
print(minf)