n= int(input())

arr = [[0]*19]*19
for i in range(n):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1
for j in range(19):
    for k in range(len(arr[j])):
        if k != 18:
            print(arr[j][k], end=" ")
        else:
            print(arr[j][k], end="\n")