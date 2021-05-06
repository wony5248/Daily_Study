import sys
input = sys.stdin.readline
N, r, c = map(int, input().split())
check = 0
isflag = 0


def solve(x, y, size):
    global check
    global isflag
    if isflag == 1:
        return
    if size == 2:
        if x == r and y == c:
            print(check)
            isflag = 1
            return
        check += 1
        if x == r and y+1 == c:
            print(check)
            isflag = 1
            return
        check += 1
        if x+1 == r and y == c:
            print(check)
            isflag = 1
            return
        check += 1
        if x+1 == r and y+1 == c:
            print(check)
            isflag = 1
            return
        check += 1
    else:
        solve(x, y, size // 2)  # 1사분면
        solve(x, y + size // 2, size // 2)  # 2사분면
        solve(x + size // 2, y, size // 2)  # 3사분면
        solve(x + size // 2, y + size // 2, size // 2)


solve(0, 0, 2 ** N)



