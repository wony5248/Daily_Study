N = int(input())
row = [input().rstrip().split() for _ in range(N)]
people = []

for i in range(N):
    for j in range(5):
        people.append([row[i][j][:1], row[i][j][2:]])                  # 줄을 서있는 순서

order = list(sorted(people, key=lambda x: (x[0], int(x[1]))))          # 티켓의 번호순으로 정렬한 순서
wait = []                                                              # 대기줄 배열

isflag = 0
i = 0
j = 0

while i < N*5:                 # 사람 서있는 배열을 다 탐색했다면 종료
    if people[i] == order[j]:              # 줄에 맨 앞사람이 들어갈 순서가 맞다면
        i += 1                             # 티켓 순 배열이랑 줄서있는 순 배열 둘다 다음칸으로
        j += 1
    elif wait and wait[-1] == order[j]:    # 대기줄에 사람이 있고 대기줄의 맨 앞사람이 들어갈 순서라면
        wait.pop()
        j += 1                             # 그사람 들여 보내고 순서 배열 다음칸으로
    else:                                  # 위의 두 경우가 아니라면
        wait.append(people[i])             # 맨 앞사람 대기열로 보냄
        i += 1                             # 줄서있는 배열 다음칸으로

while wait:                                # 다 탐색했는데 대기열이 남아 있다면
    if wait[-1] != order[j]:               # 대기열 맨 앞 사람이 들어갈 순서가 아니라면 표시해주고 종료
        isflag = 1
        break
    wait.pop()                             # if문에 안걸린다면 들여보내주고 다음 반복
    j += 1


if isflag == 0:
    print("GOOD")
else:
    print("BAD")






