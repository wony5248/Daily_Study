import sys
N = int(sys.stdin.readline())
lst = set(map(int, sys.stdin.readline().split()))      # set 은 in 메소드 시간 복잡도 O(1)  -> list = O(n)
M = int(input())
pick = list(map(int, sys.stdin.readline().split()))
for i in pick:
    if i in lst:
        print(1, end=" ")
    else:
        print(0, end=" ")


# N = int(input())
# lst = list(map(int, input().split()))
# lst.sort()
# M = input()
# pick = list(map(int, input().split()))
# def solve(num):
#     l = 0
#     r = N-1
#     while l <= r :
#         mid = (l+r)//2
#         if lst[mid] == num :
#             return 1
#         elif lst[mid] > num :
#             r = mid - 1
#         else:
#             l = mid + 1
#     return 0
#
#
# for num in pick:
#     print(solve(num), end = ' ')