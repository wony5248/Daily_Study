TC = int(input())
P = [1,1,1,2,2,3,4,5,7,9,12]
result = []
for i in range(TC):
    N = int(input())
    if len(P) > N:
        print(P[N-1])
    else:
        for j in range(N - len(P)):
            P.append(P[-1] + P[-5])
        print(P[N-1])