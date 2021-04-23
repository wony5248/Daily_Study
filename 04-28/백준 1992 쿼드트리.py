import sys
input = sys.stdin.readline
N = int(input())
video = [list(input().rstrip()) for _ in range(N)]



def solve(x, y, size):
    result = []
    if size == 1:
        return video[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if video[x][y] != video[i][j]:           # 하나라도 색이 다르다면 4등분 해줌
                result.append("(")                                    # 4등분후 각각의 사분면에 대해서 재귀로 탐색
                result.extend(solve(x, y, size // 2))             # 1사분면
                result.extend(solve(x, y+size // 2, size // 2))      # 2사분면
                result.extend(solve(x + size // 2, y, size // 2) )   # 3사분면
                result.extend(solve(x + size // 2, y + size // 2, size // 2))     # 4사분면
                result.append(")")
                return result
    return video[x][y]         # 다 같다면 해당 수 return

result = "".join(solve(0, 0, N))
print(result)

