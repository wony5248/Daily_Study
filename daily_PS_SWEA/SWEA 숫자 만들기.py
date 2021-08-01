T = int(input())

def solve(idx, tmp):
    global result
    if idx == N - 1:
        result.append(tmp)

    for i in range(4):
        if oper[i] > 0:
            oper[i] -= 1
            if i == 0:
                final = tmp + num[idx + 1]
            elif i == 1:
                final = tmp - num[idx + 1]
            elif i == 2:
                final = tmp * num[idx + 1]
            else:
                final = int(tmp / num[idx + 1])
            solve(idx + 1, final)
            oper[i] += 1
for tc in range(T):
    N = int(input())
    oper = list(map(int, input().split()))
    num = list(map(int, input().split()))
    result = []
    solve(0, num[0])
    print("#%d %d" %(tc+1, max(result)-min(result)))