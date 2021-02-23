number = int(input())
stat = list(map(int, input().split()))
stdnum = int(input())
for i in range(stdnum):
    gender, give = list(map(int, input().split()))
    if gender == 1:
        for j in range(give-1, number, give):
            if stat[j] == 0:
                stat[j] = 1
            else:
                stat[j] = 0
    elif gender == 2:
        if stat[give-1] == 0:
            stat[give-1] = 1
        elif stat[give-1] == 1:
            stat[give-1] = 0
        for j in range(1, (number+1) // 2):
            if 0 <= give - 1 - j and give - 1 + j < number:
                if stat[give - 1 - j] == stat[give - 1 + j] and stat[give - 1 - j] == 1:
                    stat[give - 1 - j] = 0
                    stat[give - 1 + j] = 0
                elif stat[give - 1 - j] == stat[give - 1 + j] and stat[give - 1 - j] == 0:
                    stat[give - 1 - j] = 1
                    stat[give - 1 + j] = 1
                elif stat[give - 1 - j] != stat[give - 1 + j]:
                    break


for i in range(number):
    if i % 20 == 0 and i != 0:
        print()
    print(stat[i], end=" ")