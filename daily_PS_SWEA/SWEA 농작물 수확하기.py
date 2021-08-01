T = int(input())
for i in range(T):
    N = int(input())
    result = 0
    farm = [list(map(int, input())) for _ in range(N)]
    num = N // 2
    for j in range(num + 1):
        result += sum(farm[j][num-j:num+j+1])
        result += sum(farm[N-j-1][num-j:num+j+1])
    final = result - sum(farm[num])

    print("#%d %d" %(i+1, final))