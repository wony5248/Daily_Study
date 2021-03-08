from itertools import combinations
import sys
while True:
    lotto = list(map(int, sys.stdin.readline().split()))
    pick = list(combinations(lotto[1:], 6))
    if lotto[0] == 0:
        break
    pick.sort()
    for i in range(len(pick)):
        for j in range(6):
            print(pick[i][j], end=" ")
        print()
    print()