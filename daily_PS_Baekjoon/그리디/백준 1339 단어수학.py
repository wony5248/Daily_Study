N = int(input())
string = [list(input()) for _ in range(N)]
alph = dict()
result = 0
for i in string:
    cnt = 0
    for j in i:
        if j not in alph:
            alph[j] = 10 ** (len(i) - 1 - cnt)
        else:
            alph[j] += 10 ** (len(i) - 1 - cnt)
        cnt += 1

sorted_alpha = sorted(list(alph.values()), reverse= True)

for i in range(len(sorted_alpha)):
    result += sorted_alpha[i] * (9 - i)
print(result)

