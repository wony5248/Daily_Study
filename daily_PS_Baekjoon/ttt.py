a = input()
score = list(map(int, input().split()))

M = max(score)
for i in range(len(score)):
    score[i] = score[i] * 100 / M

print(sum(score) / len(score))

a = 3