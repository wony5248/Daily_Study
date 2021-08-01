import re
dummy = int(input())
test1 = input()
test2 = input()
res = 0

if len(test1) > len(test2):
    A = test1
    B = test2
else:
    A = test2
    B = test1

for i in range(len(B)):
    for j in range(i+1, len(B)+1):
        if A.find(B[i:j]) != -1:
            res = max(res, len(B[i:j]))
for i in range(len(B)):
    for j in range(i+1, len(B)+1):
        if A.find(B[i:j]) != -1:
            res = max(res, len(B[i:j]))
            if res == len(B[i : j]):
                print(B[i:j])

