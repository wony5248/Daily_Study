
garo = [[0 for _ in range(10)] for _ in range(10)]
sero = [[0 for _ in range(10)] for _ in range(10)]
gresult = []
sresult = []
for i in range(10):
    garo[i] = list(map(int, input()))
# for i in range(10):
#     for j in range(10):

for i in range(10):
    for j in range(10):
        sero[i][j] = garo[j][i]

for i in range(10):
        if garo[i] == max(garo):
            gresult.append([i + 1, garo[i].index(1) + 1])
            garo[i].count(1)
            gresult.append([i + 1, garo[i].index(1) + garo[i].count(1)])
        if sero[i] == max(sero):
            sresult.append([sero[i].index(1) + 1, i + 1])
            sero[i].count(1)
            sresult.append([sero[i].index(1) + sero[i].count(1), i + 1])
if max(garo) <= max(sero):
    sresult
print(gresult)
print(sresult)
print(gresult[0][1] , sresult[0][1])

