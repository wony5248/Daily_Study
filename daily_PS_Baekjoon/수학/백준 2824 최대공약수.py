import math
N = int(input())
lstA = list(map(int, input().split()))
M = int(input())
lstB = list(map(int, input().split()))
A, B = 1, 1
for i in lstA:
    A *= i
for i in lstB:
    B *= i

print(str(math.gcd(A, B))[-9:])
