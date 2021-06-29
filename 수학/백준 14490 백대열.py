import math
N,M = input().split(":")
rgcd = math.gcd(int(N),int(M))
print("%d:%d" %(int(N)//rgcd, int(M)//rgcd))