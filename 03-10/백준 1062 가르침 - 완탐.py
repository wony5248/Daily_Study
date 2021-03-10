import sys
from itertools import combinations
from string import ascii_lowercase
N, K = map(int, sys.stdin.readline().split())
string = []
for _ in range(N):
    string.append(set(sys.stdin.readline().rstrip()[4:-4]).difference("a", "c", "i", "t", "n"))
tmp = set(ascii_lowercase).difference("a", "c", "i", "t", "n")
result = 0
# string = set(string)
if K < 5:
    result = 0
elif K == 26:
    result = N
else:
    for i in set(combinations(tmp, K-5)):
        count = 0
        for j in string:
            if not j.difference(i):
                count += 1
        result = max(result, count)
# 97~122

print(result)


















#
#
# import sys
#
# n, k = map(int, input().split())
# # a,n,t,i,c
# if k < 5:
#     print(0)
#     sys.exit(0)
#
# k -= 5
# word = [set(input()[4:-4]) for _ in range(n)]
#
# alphabet = [False] * 26
# alphabet[0] = True
# alphabet[2] = True
# alphabet[8] = True
# alphabet[13] = True
# alphabet[19] = True
# res = 0
#
#
# def cnt():
#     global n
#     temp = 0
#     for i in word:
#         for j in i:
#             if not alphabet[ord(j) - ord('a')]:
#                 break
#         else:
#             temp += 1
#     return temp
#
#
# def fill_K(s, k):
#     global res
#     if k == 0:
#         res = max(res, cnt())
#         return
#
#     for i in range(s, 26):
#         if not alphabet[i]:
#             alphabet[i] = True
#             fill_K(i + 1, k - 1)
#             alphabet[i] = False
#
#
# fill_K(0, k)
# print(res)