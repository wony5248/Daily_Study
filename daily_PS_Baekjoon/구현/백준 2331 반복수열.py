A, P = map(int, input().split())
arr = [A]
i =0
cx = 0
while True:
    x = arr[i]
    tmp = 0
    for j in str(x):
        tmp += int(j) ** P
    if tmp in arr:
        cx = tmp
        break
    else:
        arr.append(tmp)
    i += 1

print(arr.index(cx))