T = int(input())


for tc in range(T):
    n = int(input())
    udp = [0 for _ in range(n)]
    ldp = [0 for _ in range(n)]
    usticker = list(map(int, input().split()))
    lsticker = list(map(int, input().split()))
    udp[0] = usticker[0]
    ldp[0] = lsticker[0]
    udp[1] = ldp[0] + usticker[1]
    ldp[1] = udp[0] + lsticker[1]
    for i in range(2, n):
        udp[i] = max(ldp[i-1] + usticker[i], ldp[i-2] + usticker[i])     # i-1 아래꺼 + i 위꺼 고르는거랑 i-2에서 아래꺼 +i 위꺼 고르는거중 최대
        ldp[i] = max(udp[i-1] + lsticker[i], udp[i-2] + lsticker[i])     # i-1 위꺼 + i 아래꺼 vs i-2 위꺼 i 아래꺼 중 최대


    print(max(udp[n-1], ldp[n-1]))

