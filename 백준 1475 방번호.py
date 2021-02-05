N = list(map(int, input()))
import math
sticker = [0 for _ in range(10)]
for i in N:
    if i == 6:
        sticker[9] += 1
    else:
        sticker[i] += 1
sticker[9] = math.ceil(sticker[9] / 2)
minimum = max(sticker)
print(int(minimum))
