import sys
import math
from collections import Counter
N = int(sys.stdin.readline())
lst = list()
numlst = [0 for _ in range(4001)]
for _ in  range(N):
    num = int(sys.stdin.readline())
    lst.append(num)
avg = round(sum(lst) / N)
lst.sort()
med = lst[N//2]
cnt = Counter(lst).most_common()


scope = max(lst) - min(lst)
print(avg)
print(med)
if len(cnt) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(scope)