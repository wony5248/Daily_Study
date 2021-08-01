import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
party = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
customer = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]

def floyd():          # 플로이드 와샬 - A -> B 로 가는 최단시간경로 구해줌 -> party 배열은 이제 A 에서 B로 가는 최단시간 기록
    for l in range(N):
        for j in range(N):
            for k in range(N):
                if j != k and party[j][k] > party[j][l] + party[l][k]:
                    party[j][k] = party[j][l] + party[l][k]
floyd()
# print(party)
for i in range(M):
    if customer[i][2] >= party[customer[i][0]-1][customer[i][1]-1]:    # C 보다 A에서 B로 가는 시간이 짧으면
        print("Enjoy other party")
    else:
        print("Stay here")