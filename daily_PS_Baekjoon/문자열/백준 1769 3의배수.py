X = list(map(int, input()))
count = 0
while len(X) != 1:
    X = list(map(int, str(sum(X))))
    count += 1
print(count)
if X[0] % 3 == 0:
    print("YES")
else:
    print("NO")


