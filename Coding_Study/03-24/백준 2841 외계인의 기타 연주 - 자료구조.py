import sys
input = sys.stdin.readline
N, P = map(int, input().split())
guitar = [[] for _ in range(7)]
count = 0

for i in range(N):
    row, pret = map(int, input().split())
    if guitar[row] and guitar[row][-1] >= pret:             # 줄에 이미 누르고 잇는 손가락이 있고 그중 가장 큰값이 내가 누르려는 거보다 크거나 같다면
        while guitar[row] and guitar[row][-1] > pret:       # 뗄 손가락이 없거나 눌러야 하는 pret보다 누르고 있는 pret이 작을때까지
            guitar[row].pop()                            # 손 떼주고 count += 1
            count += 1
        if guitar[row] and guitar[row][-1] == pret:      # 누르려는 거와 눌려있는게 같다면
            continue
        guitar[row].append(pret)                         # 누르려는 거 눌러주고 count += 1
        count += 1
    else:                                # 누르고 있는 손가락이 없거나 누르고 있는 게 누르려는 pret 보다 작다면
        guitar[row].append(pret)    # 눌러주고 count += 1
        count += 1

print(count)
