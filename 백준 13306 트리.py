# import sys
# input = sys.stdin.readline()
#
# n, q = tuple(map(int, input()[0].split()))
# parent = [i for i in range(n+1)]
# result = []
#
# for q in input()[n:][::-1]:
#     q = q.split()
#     if len(q) == 2:
#         parent[int(q[1])] = int(input()[int(q[1]) - 1])
#     else:
#         a, b = int(q[1]), int(q[2])
#         pa, pb = parent[a], parent[b]
#         while True:
#             if parent[pa] == pa:
#                 parent[a] = pa
#                 break
#             pa = parent[pa]
#         while True:
#             if parent[pb] == pb:
#                 parent[b] = pb
#                 break
#             pb = parent[pb]
#
#         if pa == pb:
#             result.append(True)
#         else:
#             result.append(False)
#
# for re in result[::-1]:
#     if re:
#         print("YES")
#     else:
#         print("NO")

import sys

inp = sys.stdin.readlines()
n, q = tuple(map(int, inp[0].split()))
parent = [i for i in range(n + 1)]
result = []

for q in inp[n:][::-1]:
    q = q.split()
    if len(q) == 2:
        parent[int(q[1])] = int(inp[int(q[1]) - 1])
    else:
        a, b = int(q[1]), int(q[2])
        p_a, p_b = parent[a], parent[b]
        while (True):
            if parent[p_a] == p_a:
                parent[a] = p_a
                break
            p_a = parent[p_a]
        while (True):
            if parent[p_b] == p_b:
                parent[b] = p_b
                break
            p_b = parent[p_b]

        if p_a == p_b:
            result.append(True)
        else:

            result.append(False)

for re in result[::-1]:
    if re:
        print('YES')
    else:
        print('NO')