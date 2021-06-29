import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    result = []
    final = []
    bark = list(input().rstrip().split())
    while True:
        animal = list(input().rstrip().split())
        if len(animal) > 3:
            break
        result.append(animal[2])

    for j in bark:
        if j not in result:
            print(j, end=" ")
    print()

