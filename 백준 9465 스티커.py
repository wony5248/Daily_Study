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
        udp[i] = max(ldp[i-1] + usticker[i], ldp[i-2] + usticker[i])
        ldp[i] = max(udp[i-1] + lsticker[i], udp[i-2] + lsticker[i])


    print(max(udp[n-1], ldp[n-1]))

