ulim = list(map(int, input().split()))
startlink = list(map(int, input().split()))

uscore = 0
sscore = 0
isreverse = "No"
for i in range(9):
    uscore += ulim[i]
    if uscore > sscore:
        isreverse = "Yes"
    sscore += startlink[i]

print(isreverse)