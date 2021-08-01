import sys
input = sys.stdin.readline
N1, N2 = map(int, input().split())
G1 = list(input().rstrip())
G2 = list(input().rstrip())
T = int(input())
string = list(G1[::-1] + G2)
while T:
    change = set()
    for i in range(len(string)-1):
        if string[i] in G1 and string[i+1] in G2 and string[i] not in change and string[i+1] not in change:
            string[i], string[i+1] = string[i+1], string[i]
            change.add(string[i])
            change.add(string[i+1])
    T -= 1
print("".join(string))
