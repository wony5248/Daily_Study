import math
A, B, V = map(int, input().split())
final = V - A

print(math.ceil(final / (A-B)) + 1)
