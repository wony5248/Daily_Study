import math


def solution(fees, records):
    answer = []
    parktime = dict()
    content = dict()
    nm, np, mm, mp = fees
    price = []
    for i in records:
        time, num, con = i.split()
        if num not in content.keys():
            content[num] = [[time, con]]
        else:
            content[num].append([time, con])
        parktime[num] = 0

    for i in content.keys():
        if len(content[i]) % 2 == 0:
            for j in range(0, len(content[i]), 2):
                stime, smin = content[i][j][0].split(":")
                etime, emin = content[i][j + 1][0].split(":")
                if smin <= emin:
                    parktime[i] += (int(etime) - int(stime)) * 60 + int(emin) - int(smin)
                else:
                    parktime[i] += ((int(etime) - int(stime)) - 1) * 60 + int(emin) - int(smin) + 60
        else:
            for j in range(0, len(content[i]) - 1, 2):
                stime, smin = content[i][j][0].split(":")
                etime, emin = content[i][j + 1][0].split(":")
                if smin <= emin:
                    parktime[i] += (int(etime) - int(stime)) * 60 + int(emin) - int(smin)
                else:
                    parktime[i] += ((int(etime) - int(stime)) - 1) * 60 + int(emin) - int(smin) + 60
            lasttime, lastmin = content[i][-1][0].split(":")
            parktime[i] += (23 - int(lasttime)) * 60 + 59 - int(lastmin)
    for i in parktime.keys():
        totaltime = parktime[i]
        totalfee = 0
        if totaltime <= nm:
            totalfee = np
        else:
            totalfee = np + math.ceil((totaltime - nm) / mm) * mp
        price.append([i, totalfee])
    price.sort(key=lambda x: x[0])
    for i in price:
        answer.append(i[1])

    return answer