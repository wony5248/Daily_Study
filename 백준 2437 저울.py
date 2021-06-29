K = int(input())
hanoi1 = [i for i in range(1, K+1)]
hanoi2 = []
hanoi3 = []
cnt = 0


def solve(x):
    if len(hanoi3) == K and list(sorted(hanoi3)) == hanoi3:
        return


solve(cnt)