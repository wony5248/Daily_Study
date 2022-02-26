from itertools import combinations

import sys
input = sys.stdin.readline

while True:
    inp = list(input().rstrip().split())
    if inp[0] == "0":
        break
    lotto = list(combinations(inp[1:len(inp)], 6))
    for lot in lotto:
        print(" ".join(list(lot)))
    print()