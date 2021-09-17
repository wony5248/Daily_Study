import sys
input = sys.stdin.readline

left = list(input().rstrip())
M = int(input().rstrip())
right = []
for i in range(M):
    command = list(input().rstrip().split())
    if command[0] == "P":
        left.append(command[1])
    elif command[0] == "B":
        if left:
            left.pop()
    elif command[0] == "L":
        if left:
            right.append(left.pop())
    elif command[0] == "D":
        if right:
            left.append(right.pop())
print("".join(left + right[::-1]))

