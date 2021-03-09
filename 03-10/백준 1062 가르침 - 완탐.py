import sys
from itertools import combinations
from string import ascii_lowercase
N, K = map(int, sys.stdin.readline().split())

string = [(set(sys.stdin.readline().rstrip()[4:-4]).difference("a", "c", "i", "t", "n")) for _ in range(N)]
tmp = set(ascii_lowercase).difference("a", "c", "i", "t", "n")
result = 0

# def solve():


if K < 5:
    result = 0
elif K == 26:
    result = N

# 97~122

print(tmp)