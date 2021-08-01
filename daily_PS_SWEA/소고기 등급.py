N = int(input())

cowdic = {
    "A":[0 for i in range(N)],
    "B":[0 for i in range(N)],
    "C":[0 for i in range(N)],
    "D":[0 for i in range(N)]
}
common = [0 for i in range(N)]
count =0
for i in range(N):
    cow = input().split()
    cowdic[cow[1]][i] = cow[0]
grade = input()
for i in range(N):
    if cowdic[grade][i] not in common and cowdic[grade] !=0:
        print(cowdic[grade][i], end=" ")
    common[i] = cowdic[grade][i]



