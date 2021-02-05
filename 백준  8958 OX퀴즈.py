from collections import deque
TC = int(input())

for i in range(TC):
    count = 0
    queue = deque()
    result = deque()
    string = input()
    for j in range(len(string)):
        queue.append(string[j])
    while queue:
        if queue.popleft() == "O":
            result.append("O")
        elif queue.popleft() == "X":
            for k in range(1, len(result)+1):
                count += k
    print(count)