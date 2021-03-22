import sys
input = sys.stdin.readline
N, P = map(int, input().split())
guitar = [[] for _ in range(7)]
count = 0
for i in range(N):
    isflag = 0
    row, pret = map(int, input().split())
    if guitar[row]:
        for j in range(len(guitar[row])):
            if pret < guitar[row][j]:
                count += 1
                del guitar[row][j]
                guitar[row].insert(j, 0)
                guitar[row].append(pret)
            elif pret == guitar[row][j]:
                count += 1
            else:
                isflag = 1

        if isflag == 1:
            count += 1
            guitar[row].append(pret)
    else:
        count += 1
        guitar[row].append(pret)
print(count)