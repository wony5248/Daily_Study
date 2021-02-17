score = []
sindex = []
for i in range(8):
    score.append(int(input()))
sscore = sorted(score)
length = len(sscore)
print(sum(sscore[length-5:length]))
for i in range(5):
    maxs = max(score)
    for j in range(len(score)):
        if score[j] == maxs:
            sindex.append(j+1)
            score[j] = 0
sindex.sort()
for i in range(5):
    print((sindex[i]), end=" ")