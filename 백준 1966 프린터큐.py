T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    P = list(map(int, input().split()))
    queue = [0 for _ in range(N)]
    queue[M] = 1
    count = 0
    while True:
        if P[0] == max(P):
            count+=1
            if queue[0] == 1:
                print(count)
                break
            else:
                del P[0]
                del queue[0]
        else:
            P.append(P[0])
            del P[0]
            queue.append(queue[0])
            del queue[0]

